# Gilded Rose – Python Solution (Refactored with Helpers)

This repository contains my solution to the **Gilded Rose** 

The objective is to update each item’s `sell_in` and `quality` values once per day, following a set of business rules for special items such as **Aged Brie**, **Backstage passes**, **Sulfuras**, and **Conjured** items.

## Summary of the Business Rules Implemented

All items have:
- `sell_in`: number of days remaining to sell the item
- `quality`: value of the item

General rules:
- At the end of each day, most items decrease in `sell_in` and `quality`.
- Once the sell-by date has passed (`sell_in < 0`), most items degrade **twice as fast**.
- `quality` is never negative.
- `quality` is never more than `50` (except Sulfuras).

Special items:
- **Aged Brie**: increases in quality as it gets older (faster after expiry).
- **Backstage passes**:
  - increases in quality as the concert approaches
  - +2 when there are 10 days or less
  - +3 when there are 5 days or less
  - quality drops to 0 after the concert
- **Sulfuras**: never decreases in quality and never changes `sell_in`.
- **Conjured**: degrades in quality **twice as fast as normal items**
  - before expiry: `-2` per day
  - after expiry: `-4` per day total (explained below)

## How Conjured Expiry Works (Why It Becomes “-4”)

Conjured items degrade twice as fast as normal items:
- Normal item:
  - before expiry: `-1`
  - after expiry: `-2` total (`-1` daily + `-1` expired)
- Conjured item:
  - before expiry: `-2`
  - after expiry: `-4` total (`-2` daily + `-2` expired)

In this solution, this is implemented as:
- a **daily quality update**
- and then an **expired quality change** applied only when `sell_in < 0` after decrementing `sell_in`



- Contains the `GildedRose` class and the main `update_quality()` loop.
- The loop is responsible for orchestration only:
  - identify item type
  - apply daily quality change
  - decrement sell_in (except Sulfuras)
  - apply expired adjustment


- `item_type(name)`  
  Classifies an item into one of: `normal`, `brie`, `backstage`, `sulfuras`, `conjured`.  

- `daily_quality_change(item_type, sell_in)`  
  Returns the daily quality delta for the item type, based on current `sell_in`.

- `expired_quality_change(item_type)`  
  Returns the additional change applied once the item has expired (`sell_in < 0` after decrement).

- `apply_quality_change(quality, change)`  
  Applies the change and clamps the result to `[0, 50]`:

## Running the unit tests from the Command-Line

```
python -m unittest
```

## Running the example simulation from the Command-Line

For e.g. 10 days:

```
python example_simulation.py 10
```

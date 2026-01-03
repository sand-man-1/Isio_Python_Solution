from src.helpers import apply_quality_change, daily_quality_change, expired_quality_change, item_type

class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items: 
            #generrally i refactpred the code to use a more functional approach, and quite modular
            kind = item_type(item.name)
            #after determinging the item type, changes will be applied based on that
            if kind == "sulfuras":
                continue # handle sulfura easily by skipping it

            # quality updateworks by taking the current quality and applying the changes based on the type and sell_in
            item.quality = apply_quality_change(item.quality, daily_quality_change(kind, item.sell_in))
            item.sell_in -= 1

            #after reducing sell_in, we check if the item is expired and apply further changes if needed 
            # so each item giws through two phases of quality update: daily and expired if applicable
            if item.sell_in < 0:
                if kind == "backstage":
                    item.quality = 0 #changeto 0 directly for backstage passes
                else:
                    item.quality = apply_quality_change(item.quality, expired_quality_change(kind))
                    # for other items, apply the expired quality change







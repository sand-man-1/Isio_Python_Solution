def item_type(name):
    if name.startswith("Aged Brie"):
        return "brie"
    if name.startswith("Backstage passes"):
        return "backstage"
    if name.startswith("Sulfuras"):
        return "sulfuras"
    if name.startswith("Conjured"):
        return "conjured"
    return "normal"


def daily_quality_change(item_type, sell_in):
    if item_type == "brie":
        return 1 #brie increases by 1 daily
    if item_type == "backstage":
        if sell_in < 6:
            return 3
        if sell_in < 11:
            return 2
        return 1 #handle backstage passes increases
    if item_type == "conjured":
        return -2 #new conjured degrades twice as fast
    return -1 #notmal items degrade by 1 daily


def expired_quality_change(item_type):
    if item_type == "brie":
        return 1 #brie increases by 1 after expiration
    if item_type == "conjured":
        return -2   #conjured degrades twice as fast after expiration
    return -1


def apply_quality_change(quality, change):
    return max(0, min(50, quality + change))
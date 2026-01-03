import sys
from pathlib import Path

# Add parent directory to path so imports work when running this file directly
sys.path.insert(0, str(Path(__file__).parent.parent))

import unittest

from src.gilded_rose import GildedRose
from src.models import Item
from src.helpers import apply_quality_change, daily_quality_change, expired_quality_change, item_type


class GildedRoseTest(unittest.TestCase):
    def test_normal_item_decreases(self):
        items = [Item("Elixir of the Mongoose", 5, 7)]
        GildedRose(items).update_quality()
        self.assertEqual(4, items[0].sell_in)
        self.assertEqual(6, items[0].quality)

    def test_normal_item_degrades_twice(self):
        items = [Item("Elixir of the Mongoose", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(8, items[0].quality)

    def test_aged_brie_increases_qual(self):
        items = [Item("Aged Brie", 10, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(21, items[0].quality)
    
    def test_aged_brie_quality_check(self):
        items = [Item("Aged Brie", 10, 50)]
        GildedRose(items).update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(50, items[0].quality)
    
    def test_backstage_pass_increases(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 11, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(10, items[0].sell_in)
        self.assertEqual(21, items[0].quality)

    def test_backstage_pass_quality_drops(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 20)]
        GildedRose(items).update_quality()
        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(0, items[0].quality)
    
    def test_sulfuras(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 0, 80)]
        GildedRose(items).update_quality()
        self.assertEqual(0, items[0].sell_in)
        self.assertEqual(80, items[0].quality)
    
    def test_conjured_item_degrades_twice(self):
        items = [Item("Conjured Mana Cake", 3, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(2, items[0].sell_in)
        self.assertEqual(8, items[0].quality)  

    def test_conjured_item_degrades_four(self):
        items = [Item("Conjured Mana Cake", 0, 10)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(-1, items[0].sell_in)
        self.assertEqual(6, items[0].quality)  

        
if __name__ == '__main__':
    unittest.main()

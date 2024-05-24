#!/usr/bin/env python3
"""Define the class LFUCache that inherits from BaseCaching
and is a caching system"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Represent a basic caching system with a LFU implementation"""
    def __init__(self):
        """initialize data and variables for the cahing system"""
        super().__init__()
        self.item_positions = []

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value"""
        if key is not None and item is not None:
            if self.cache_data.get(key):
                self.item_positions.remove(key)
                self.cache_data.pop(key)
            self.cache_data[key] = item
            self.item_positions.append(key)
            elmt_count = len(self.cache_data.items())
            if elmt_count > super().MAX_ITEMS:
                discard_key = self.item_positions[0]
                self.cache_data.pop(discard_key)
                self.item_positions.remove(discard_key)
                print("DISCARD: {}".format(discard_key))

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None or key not in self.cache_data.keys():
            return None
        self.item_positions.remove(key)
        self.item_positions.append(key)
        return self.cache_data.get(key)

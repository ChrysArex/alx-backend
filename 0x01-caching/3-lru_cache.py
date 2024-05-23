#!/usr/bin/env python3
"""Define the class LRUCache that inherits from BaseCaching
and is a caching system"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Represent a basic caching system with a LRU implementation"""
    def __init__(self):
        """initialize data and variables for the cahing system"""
        super().__init__()
        self.use_count = {}

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value"""
        if key is not None and item is not None:
            if self.cache_data.get(key):
                self.cache_data.pop(key)
                self.use_count
            self.cache_data[key] = item
            elmt_count = len(self.cache_data.items())
            if elmt_count > super().MAX_ITEMS:
                discard_key = list(self.cache_data.keys())[elmt_count - 2]
                self.cache_data.pop(discard_key)
                print("DISCARD: {}".format(discard_key))

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None:
            return None
        return self.cache_data.get(key)

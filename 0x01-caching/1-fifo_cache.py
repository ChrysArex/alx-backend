#!/usr/bin/env python3
"""Define the class FIFOCache that inherits from BaseCaching
and is a caching system"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Represent a basic caching system"""
    def __init__(self):
        """initialize data and variables for the cahing system"""
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data.items()) > super().MAX_ITEMS:
                discard_key = list(self.cache_data.keys())[0]
                self.cache_data.pop(list(self.cache_data.keys())[0])
                print("DISCARD: {}".format(discard_key))

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None:
            return None
        return self.cache_data.get(key)

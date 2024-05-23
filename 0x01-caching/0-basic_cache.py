#!/usr/bin/env python3
"""Define the class BasicCache that inherits from BaseCaching
and is a caching system"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Represent a basic caching system"""
    def __init__(self):
        """initialize data and variables for the cahing system"""
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data the item value"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """return the value in self.cache_data linked to key"""
        if key is None:
            return None
        return self.cache_data.get(key)

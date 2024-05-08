#!/usr/bin/env python3
"""
   Basic Cache Class
"""
OrderedDict = __import__('collections').OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ LIFO caching logic """

    def __init__(self):
        """ init logic"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item
        if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
            last_in_key, _ = self.cache_data.popitem(True)
            print("DISCARD:", last_in_key)

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)

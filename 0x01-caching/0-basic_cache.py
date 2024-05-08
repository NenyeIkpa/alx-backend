#!/usr/bin/env/python3
"""
   Basic Cache Class
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ basing caching logic """

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            self.cache_data[key] = value

    def get(self, key):
        """ Get an item by key """
        if key not in self.cache_data or key is None:
            return None
        return self.cache_data.get(key)

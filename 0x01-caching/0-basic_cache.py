#!/usr/bin/env python3
"""
   Basic Cache Class
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ basing caching logic """

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            self.cache_data[key] = value

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)

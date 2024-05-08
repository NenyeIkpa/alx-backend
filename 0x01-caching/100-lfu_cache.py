#!/usr/bin/env python3
"""
   LFU Caching Module
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Represents an object that allows storing and
    retrieving items from a dictionary with a LFU
    pattern
    """
    def __init__(self):
        """Initializes the cache.
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.freq_keys = []

    def __reorder_items(self, mru_key):
        """Reorders the items in this cache based on the most
        recently used item.
        """
        max_positions = []
        mru_freq = 0
        mru_position = 0
        insert_position = 0
        for x, freq_key in enumerate(self.freq_keys):
            if freq_key[0] == mru_key:
                mru_freq = freq_key[1] + 1
                mru_position = x
                break
            elif len(max_positions) == 0:
                max_positions.append(x)
            elif freq_key[1] < self.freq_keys[max_positions[-1]][1]:
                max_positions.append(i)
        max_positions.reverse()
        for position in max_positions:
            if self.freq_keys[position][1] > mru_freq:
                break
            insert_position = position
        self.freq_keys.pop(mru_position)
        self.freq_keys.insert(insert_position, [mru_key, mru_freq])

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                lfu_key, _ = self.keys_freq[-1]
                self.cache_data.pop(lfu_key)
                self.freq_keys.pop()
                print("DISCARD:", lfu_key)
            self.cache_data[key] = item
            insert_index = len(self.freq_keys)
            for y, freq_key in enumerate(self.freq_keys):
                if freq_key[1] == 0:
                    insert_index = y
                    break
            self.freq_keys.insert(insert_index, [key, 0])
        else:
            self.cache_data[key] = item
            self.__reorder_items(key)

    def get(self, key):
        """Retrieves an item by key.
        """
        if key is not None and key in self.cache_data:
            self.__reorder_items(key)
        return self.cache_data.get(key, None)

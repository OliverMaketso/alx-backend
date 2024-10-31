#!/usr/bin/env python3
"""
This module contains a class BasicCache that inherits from BaseCaching
and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache is a caching system that has no limit """

    def put(self, key, item):
        """ Add an item to the cache if key and item are not None """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieve an item by key, return None if key doesn't exist """
        return self.cache_data.get(key, None)

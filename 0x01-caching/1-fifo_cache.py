#!/usr/bin/env python3
"""
FIFOCache class module
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines a caching system with FIFO eviction policy """
    def __init__(self):
        """Initiaize the cache"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Assigns the item value to the cache with the specified"""
        if key is None or item is None:
            return

        if key not in self.cache_data:
            # If adding this key exceeds the limit, discard the first item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # FIFO: pop the first inserted item
                oldest_key = self.order.pop(0)
                del self.cache_data[oldest_key]
                print(f"DISCARD: {oldest_key}")

        # Add the new item to the cache and track the insertion order
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Return the value linked to the key"""
        return self.cache_data.get(key, None)

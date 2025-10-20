# LeetCode 146: LRU Cache
# Explanation:
# 1. Implement a Least Recently Used (LRU) cache with O(1) time for get and put.
# 2. Use OrderedDict to maintain insertion order — most recently used items move to the end.
# 3. When capacity is exceeded, remove the least recently used item (first one).
# Time Complexity: O(1) for both get and put.
# Space Complexity: O(capacity)

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

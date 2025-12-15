# LeetCode 380: Insert Delete GetRandom O(1)
# Explanation:
# 1. Use list to store elements for random access.
# 2. Use dict to map value -> index for O(1) insert/delete.
# 3. On remove, swap with last element to maintain O(1).
# Time Complexity: O(1) average
# Space Complexity: O(n)

import random

class RandomizedSet:
    def __init__(self):
        self.val_to_index = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        self.val_to_index[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_index:
            return False
        idx = self.val_to_index[val]
        last_val = self.values[-1]
        self.values[idx] = last_val
        self.val_to_index[last_val] = idx
        self.values.pop()
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)

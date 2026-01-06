# LeetCode 381: Insert Delete GetRandom O(1) - Duplicates allowed
# Explanation:
# 1. values: list of elements
# 2. val_to_indices: dict of val -> set of indices
# 3. On remove, swap with last element to maintain O(1)
# Time Complexity: O(1) average
# Space Complexity: O(n)

import random
from collections import defaultdict

class RandomizedCollection:
    def __init__(self):
        self.values = []
        self.val_to_indices = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.values.append(val)
        self.val_to_indices[val].add(len(self.values)-1)
        return len(self.val_to_indices[val]) == 1

    def remove(self, val: int) -> bool:
        if val not in self.val_to_indices or not self.val_to_indices[val]:
            return False
        remove_idx = self.val_to_indices[val].pop()
        last_val = self.values[-1]
        self.values[remove_idx] = last_val
        self.val_to_indices[last_val].add(remove_idx)
        self.val_to_indices[last_val].discard(len(self.values)-1)
        self.values.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)

rc = RandomizedCollection()
print(rc.insert(1))  # True
print(rc.insert(1))  # False
print(rc.insert(2))  # True
print(rc.getRandom()) # 1 or 2 (1 has higher probability)
print(rc.remove(1))  # True
print(rc.getRandom()) # 1 or 2

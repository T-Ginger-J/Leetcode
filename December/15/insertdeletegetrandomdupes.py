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


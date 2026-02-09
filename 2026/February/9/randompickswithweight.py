from typing import List
import random
import bisect


class Solution:

    # -------------------------------------------------------
    # Method 1: Prefix Sum + Binary Search (Optimal)
    # -------------------------------------------------------
    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        # Binary search for the first prefix >= target
        idx = bisect.bisect_left(self.prefix, target)
        return idx


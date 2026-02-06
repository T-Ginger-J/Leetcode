import random


class Solution:

    # -------------------------------------------------------
    # Method 1: Hash Map + Shuffle (Optimal)
    # -------------------------------------------------------
    def __init__(self, m: int, n: int):

        self.m = m
        self.n = n
        self.total = m * n
        self.remaining = self.total

        # Map for virtual swaps
        self.map = {}

    def flip(self):

        # Pick random index from remaining range
        r = random.randint(0, self.remaining - 1)

        # Get actual position
        idx = self.map.get(r, r)

        # Decrease remaining pool
        self.remaining -= 1

        # Move last available index to r
        self.map[r] = self.map.get(self.remaining, self.remaining)

        return [idx // self.n, idx % self.n]

    def reset(self):

        self.remaining = self.total
        self.map.clear()


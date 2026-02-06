# LeetCode 519: Random Flip Matrix
# Explanation:
# 1. We have an m x n binary matrix initially filled with 0.
# 2. Each call to flip() randomly chooses a cell with value 0 and sets it to 1.
# 3. All zero cells must have equal probability of being chosen.
# 4. reset() restores the matrix to all zeros.

# Methods Used:
# - Hash Map + Fisher-Yates Shuffle Simulation
# - Virtual 1D Index Mapping

# Key Idea:
# - Treat the matrix as a flattened array of size m*n.
# - Maintain a shrinking range [0, total-1].
# - Randomly pick an index in this range.
# - Use a map to simulate swaps.

# Time Complexity:
# - flip(): O(1) average
# - reset(): O(1)

# Space Complexity:
# - O(k), k = number of flipped cells


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


# -------------------------------------------------------
# Examples (Including Edge Cases)
# -------------------------------------------------------

# Example 1
obj = Solution(2, 3)

print(obj.flip())   # Random free cell
print(obj.flip())   # Random free cell
print(obj.flip())   # Random free cell

obj.reset()

print(obj.flip())   # Random free cell after reset


# Example 2 (Single Cell)
obj2 = Solution(1, 1)

print(obj2.flip())  # [0, 0]
obj2.reset()
print(obj2.flip())  # [0, 0]


# Example 3 (Large Matrix Simulation)
obj3 = Solution(3, 3)

res = set()
for _ in range(9):
    res.add(tuple(obj3.flip()))

print(len(res))     # 9 (all unique)

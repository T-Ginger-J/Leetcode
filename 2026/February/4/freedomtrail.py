# LeetCode 514: Freedom Trail
# Explanation:
# 1. We are given a circular ring and a target key.
# 2. At each step, we can rotate the ring clockwise or counterclockwise
#    to align the desired character at position 0, then press the button.
# 3. Each rotation step costs 1, and each button press costs 1.
# 4. Goal: minimize total steps to spell the key.

# Methods Used:
# - Dynamic Programming with Memoization (DFS + Cache)
# - State: (current_ring_index, key_index)
# - For each character in key, try all matching positions in ring.

# Time Complexity:
# - O(n * m * k)
#   n = len(ring), m = len(key), k = avg occurrences of each char
#   (practically optimized by memoization)

# Space Complexity:
# - O(n * m) for memo table


from functools import lru_cache
from collections import defaultdict


class Solution:

    # -------------------------------------------------------
    # Method 1: Top-Down DP (Memoization) - Optimal
    # -------------------------------------------------------
    def findRotateSteps(self, ring: str, key: str) -> int:

        n = len(ring)

        # Map each character to its positions in ring
        pos = defaultdict(list)
        for i, ch in enumerate(ring):
            pos[ch].append(i)

        @lru_cache(None)
        def dfs(ring_idx, key_idx):

            # Finished spelling key
            if key_idx == len(key):
                return 0

            res = float("inf")

            # Try all positions matching current key character
            for p in pos[key[key_idx]]:

                dist = abs(p - ring_idx)
                step = min(dist, n - dist)   # circular distance

                # +1 for button press
                res = min(
                    res,
                    step + 1 + dfs(p, key_idx + 1)
                )

            return res

        return dfs(0, 0)

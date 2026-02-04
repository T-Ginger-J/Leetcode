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

    # -------------------------------------------------------
    # Method 2: Bottom-Up DP
    # -------------------------------------------------------
    def findRotateStepsDP(self, ring: str, key: str) -> int:

        n = len(ring)
        m = len(key)

        pos = defaultdict(list)
        for i, ch in enumerate(ring):
            pos[ch].append(i)

        # dp[i][j] = min cost to spell key[i:] when ring at j
        dp = [[float("inf")] * n for _ in range(m + 1)]

        # Base case
        for j in range(n):
            dp[m][j] = 0

        for i in range(m - 1, -1, -1):

            for j in range(n):

                for p in pos[key[i]]:

                    dist = abs(p - j)
                    step = min(dist, n - dist)

                    dp[i][j] = min(
                        dp[i][j],
                        step + 1 + dp[i + 1][p]
                    )

        return dp[0][0]


# -------------------------------------------------------
# Examples (Including Edge Cases)
# -------------------------------------------------------

# Example 1
# ring = "godding", key = "gd"
# Steps: g->g (press), rotate to d (1), press
print(Solution().findRotateSteps("godding", "gd"))  # 4


# Example 2
# Multiple rotations
print(Solution().findRotateSteps("abcde", "ade"))  # 6


# Example 3 (Repeated Characters)
# ring = "aaa", key = "aa"
# Always aligned, just press twice
print(Solution().findRotateSteps("aaa", "aa"))  # 2


# Example 4 (Single Character Ring)
# Only presses
print(Solution().findRotateSteps("a", "aaaa"))  # 4


# Example 5 (Full Rotation Needed)
print(Solution().findRotateSteps("ab", "ba"))  # 4

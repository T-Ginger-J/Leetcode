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

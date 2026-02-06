from functools import lru_cache
from typing import List


class Solution:

    # -------------------------------------------------------
    # Method 1: 1D DP (Space Optimized) - Optimal
    # -------------------------------------------------------
    def change1D(self, amount: int, coins: List[int]) -> int:

        dp = [0] * (amount + 1)
        dp[0] = 1

        # Iterate coins first to avoid permutations
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]

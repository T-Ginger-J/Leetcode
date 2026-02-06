# LeetCode 518: Coin Change II
# Explanation:
# 1. We are given coins of different denominations and a target amount.
# 2. We need to count how many combinations can make up the amount.
# 3. Each coin can be used unlimited times.
# 4. Order does NOT matter (combinations, not permutations).

# Methods Used:
# - 1D Bottom-Up Dynamic Programming (Unbounded Knapsack)
# - 2D DP Table (Classic Formulation)
# - Top-Down DP with Memoization

# Time Complexity:
# - All methods: O(n * amount), n = number of coins

# Space Complexity:
# - 1D DP: O(amount)
# - 2D DP: O(n * amount)
# - Memoization: O(n * amount)


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

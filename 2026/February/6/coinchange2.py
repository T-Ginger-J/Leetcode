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

    # -------------------------------------------------------
    # Method 2: 2D DP (Classic Knapsack)
    # -------------------------------------------------------
    def change2D(self, amount: int, coins: List[int]) -> int:

        n = len(coins)

        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        # Base case
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(amount + 1):

                # Not use coin
                dp[i][j] = dp[i - 1][j]

                # Use coin (unlimited)
                if j >= coins[i - 1]:
                    dp[i][j] += dp[i][j - coins[i - 1]]

        return dp[n][amount]

    # -------------------------------------------------------
    # Method 3: Top-Down DP (Memoization)
    # -------------------------------------------------------
    def changeMemo(self, amount: int, coins: List[int]) -> int:

        n = len(coins)

        @lru_cache(None)
        def dfs(i, remain):

            if remain == 0:
                return 1

            if remain < 0 or i == n:
                return 0

            # Choose or skip current coin
            return dfs(i, remain - coins[i]) + dfs(i + 1, remain)

        return dfs(0, amount)


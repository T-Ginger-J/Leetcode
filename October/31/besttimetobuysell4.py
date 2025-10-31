# LeetCode 188: Best Time to Buy and Sell Stock IV
# Explanation:
# 1. If k >= len(prices)//2, treat as infinite transactions (use greedy sum of profits).
# 2. Otherwise, use DP where dp[i][j] = max profit using i transactions up to day j.
# 3. Track best_buy = max(dp[i-1][m] - prices[m]) to optimize transitions.
# Time Complexity: O(k * n)
# Space Complexity: O(k * n)

class Solution:
    def maxProfit(self, k: int, prices: list[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0
        if k >= n // 2:
            return sum(max(prices[i+1] - prices[i], 0) for i in range(n-1))
        
        dp = [[0] * n for _ in range(k+1)]
        for i in range(1, k+1):
            best_buy = -prices[0]
            for j in range(1, n):
                dp[i][j] = max(dp[i][j-1], prices[j] + best_buy)
                best_buy = max(best_buy, dp[i-1][j-1] - prices[j])
        return dp[k][n-1]

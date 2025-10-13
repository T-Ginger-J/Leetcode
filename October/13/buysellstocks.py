# LeetCode 121: Best Time to Buy and Sell Stock
# Explanation:
# 1. Track the minimum price seen so far.
# 2. At each price, compute potential profit = current_price - min_price.
# 3. Keep the maximum profit encountered.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices):
        min_price = float('inf')
        max_profit = 0
        for p in prices:
            min_price = min(min_price, p)
            max_profit = max(max_profit, p - min_price)
        return max_profit

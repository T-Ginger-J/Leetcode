# LeetCode 122: Best Time to Buy and Sell Stock II
# Explanation:
# 1. You can make as many transactions as you like (buy one and sell one share multiple times).
# 2. The key is to sum up all positive price differences between consecutive days.
# 3. This effectively captures every profitable transaction.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices):
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit

    def maxProfitGreedy(self, prices):
        return sum(max(prices[i] - prices[i - 1], 0) for i in range(1, len(prices)))

print(Solution().maxProfit([7,1,5,3,6,4]))
# Output: 7 (Buy at 1→Sell at 5, Buy at 3→Sell at 6)

print(Solution().maxProfit([1,2,3,4,5]))
# Output: 4 (Buy at 1→Sell at 5)

print(Solution().maxProfit([7,6,4,3,1]))
# Output: 0 (No profitable trades)

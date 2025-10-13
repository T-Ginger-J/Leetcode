# LeetCode 123: Best Time to Buy and Sell Stock III
# Explanation:
# 1. You may complete at most TWO transactions.
# 2. Use DP with four states:
#    - buy1: max profit after first buy
#    - sell1: max profit after first sell
#    - buy2: max profit after second buy
#    - sell2: max profit after second sell
# 3. For each price, update these states accordingly.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices):
        buy1, sell1 = float('-inf'), 0
        buy2, sell2 = float('-inf'), 0
        for p in prices:
            buy1 = max(buy1, -p)         # Buy first stock
            sell1 = max(sell1, buy1 + p) # Sell first stock
            buy2 = max(buy2, sell1 - p)  # Buy second stock
            sell2 = max(sell2, buy2 + p) # Sell second stock
        return sell2

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

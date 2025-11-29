# LeetCode 309: Best Time to Buy and Sell Stock with Cooldown
# Explanation:
# 1. Use DP to track 3 states:
#    - hold: max profit holding a stock
#    - sold: max profit just sold a stock
#    - rest: max profit in cooldown or do nothing
# 2. Transition:
#    hold = max(hold, rest - price)
#    sold = hold + price
#    rest = max(rest, sold_prev)
# 3. Answer = max(sold, rest)
# Time Complexity: O(n), iterate once over prices
# Space Complexity: O(1), using variables for states

class Solution:
    def maxProfit(self, prices):
        if not prices: return 0
        hold = -prices[0]
        sold = 0
        rest = 0
        for price in prices[1:]:
            prev_sold = sold
            sold = hold + price
            hold = max(hold, rest - price)
            rest = max(rest, prev_sold)
        return max(sold, rest)

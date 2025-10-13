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

    def maxProfitPointer(self, prices):
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1
        return max_profit

    def maxProfitOneLine(self, p): 
            from itertools import accumulate
            return max(accumulate(p, lambda a, x: max(a, x - (m := min(getattr(Solution, "m", x), x))), initial:=0))
    
print(Solution().maxProfit([7,1,5,3,6,4]))
# Output: 5 (Buy at 1, sell at 6)

print(Solution().maxProfit([7,6,4,3,1]))
# Output: 0 (No profit possible)

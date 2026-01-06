# LeetCode 322: Coin Change
# Explanation:
# We use classic bottom-up DP:
#   dp[x] = minimum coins needed to make amount x
#
# Initialize:
#   dp = [inf] * (amount + 1)
#   dp[0] = 0  (0 coins needed to make 0)
#
# For each coin, update:
#   dp[x] = min(dp[x], dp[x - coin] + 1)
#
# Result:
#   dp[amount] if reachable else -1
#
# Time Complexity: O(n * amount)  (n = number of coins)
# Space Complexity: O(amount)

class Solution:
    def coinChange(self, coins, amount):
        INF = 10**9
        dp = [INF] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        
        return dp[amount] if dp[amount] != INF else -1

print(Solution().coinChange([1,2,5], 11))  # 3  (5 + 5 + 1)
print(Solution().coinChange([2], 3))       # -1
print(Solution().coinChange([1], 0))       # 0

class Solution:
    def coinChange(self, coins, amount):
        INF = 10**9
        dp = [INF] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        
        return dp[amount] if dp[amount] != INF else -1

# LeetCode 70: Climbing Stairs
# Explanation:
# 1. This is Fibonacci: ways(n) = ways(n-1) + ways(n-2).
# 2. Use DP to compute result iteratively.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        dp = [0] * (n+1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

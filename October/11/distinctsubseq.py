# LeetCode 115: Distinct Subsequences
# Explanation:
# 1. Count how many distinct subsequences of `s` equal string `t`.
# 2. Use dynamic programming:
#    - dp[i][j] = number of ways first i chars of `s` form first j chars of `t`.
#    - If s[i-1] == t[j-1], then:
#         dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
#      Else:
#         dp[i][j] = dp[i-1][j]
# 3. Initialize dp[i][0] = 1 since empty t is always a subsequence.
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(m + 1):
            dp[i][0] = 1
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        return dp[m][n]

from functools import lru_cache


class Solution:

    # -------------------------------------------------------
    # Method 1: Interval DP (Bottom-Up) - Optimal
    # -------------------------------------------------------
    def longestPalindromeSubseqDP(self, s: str) -> int:

        n = len(s)

        if n == 0:
            return 0

        dp = [[0] * n for _ in range(n)]

        # Length 1 substrings
        for i in range(n):
            dp[i][i] = 1

        # Build by increasing length
        for length in range(2, n + 1):

            for i in range(n - length + 1):

                j = i + length - 1

                if s[i] == s[j]:

                    if length == 2:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i + 1][j - 1] + 2

                else:
                    dp[i][j] = max(
                        dp[i + 1][j],
                        dp[i][j - 1]
                    )

        return dp[0][n - 1]

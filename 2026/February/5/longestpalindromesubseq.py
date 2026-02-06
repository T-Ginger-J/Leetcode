# LeetCode 516: Longest Palindromic Subsequence
# Explanation:
# 1. Given a string s, find the length of the longest subsequence that is a palindrome.
# 2. A subsequence does not need to be contiguous.
# 3. We use Dynamic Programming on intervals.

# Methods Used:
# - Bottom-Up DP on Substrings
# - Top-Down DP with Memoization
# - LCS Reduction (LPS = LCS(s, reverse(s)))

# Time Complexity:
# - All methods: O(n^2)

# Space Complexity:
# - Interval DP: O(n^2)
# - Optimized LCS: O(n)


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

    # -------------------------------------------------------
    # Method 2: Top-Down DP (Memoization)
    # -------------------------------------------------------
    def longestPalindromeSubseqMemo(self, s: str) -> int:

        @lru_cache(None)
        def dfs(l, r):

            if l > r:
                return 0
            if l == r:
                return 1

            if s[l] == s[r]:
                return dfs(l + 1, r - 1) + 2

            return max(
                dfs(l + 1, r),
                dfs(l, r - 1)
            )

        return dfs(0, len(s) - 1)


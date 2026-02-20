# LeetCode 583: Delete Operation for Two Strings
# Explanation:
# 1. Given two strings word1 and word2, return the minimum number of steps to make them the same by deleting characters.
# 2. Approach:
#    - Use dynamic programming to find the length of the Longest Common Subsequence (LCS).
#    - Minimum deletions = len(word1) + len(word2) - 2 * LCS
# 3. Time Complexity: O(m * n), m = len(word1), n = len(word2)
# 4. Space Complexity: O(m * n), can be optimized to O(n)

from typing import List

class Solution:

    # -------------------------------------------------------
    # Method 1: DP table
    # -------------------------------------------------------
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                if word1[i] == word2[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        lcs = dp[m][n]
        return m + n - 2*lcs

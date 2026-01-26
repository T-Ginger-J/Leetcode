# LeetCode 474: Ones and Zeroes
# Explanation:
# Given an array of binary strings strs and two integers m and n,
# return the size of the largest subset such that there are at most
# m zeros and n ones in the subset.
#
# Method 1: 0/1 Knapsack DP (2D)
# - Treat zeros as one cost dimension and ones as another.
# - dp[i][j] = max subset size with i zeros and j ones.
# - Iterate strings and update dp backwards to avoid reuse.
#
# Time Complexity: O(len(strs) * m * n)
# Space Complexity: O(m * n)

from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zeros = s.count('0')
            ones = s.count('1')
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zeros][j - ones] + 1)

        return dp[m][n]

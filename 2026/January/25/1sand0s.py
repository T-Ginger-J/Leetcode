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


# Alternate Python Solution: 3D DP (More Explicit State)
# - dp[k][i][j]: using first k strings, max subset size with i zeros and j ones.
# - Easier to reason about but worse space complexity.

class Solution3D:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        length = len(strs)
        dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(length + 1)]

        for k in range(1, length + 1):
            zeros = strs[k - 1].count('0')
            ones = strs[k - 1].count('1')
            for i in range(m + 1):
                for j in range(n + 1):
                    dp[k][i][j] = dp[k - 1][i][j]
                    if i >= zeros and j >= ones:
                        dp[k][i][j] = max(
                            dp[k][i][j],
                            dp[k - 1][i - zeros][j - ones] + 1
                        )
        return dp[length][m][n]


# Additional Examples (Edge Cases and Non-LeetCode Examples)

sol = Solution()

# Example 1: Exact fit
print(sol.findMaxForm(["10", "0", "1"], 1, 1))
# Expected output: 2  ("0", "1")

# Example 2: Zero capacity
print(sol.findMaxForm(["0", "00", "1"], 0, 1))
# Expected output: 1  ("1")

# Example 3: Large budget, small set
print(sol.findMaxForm(["01", "10", "001"], 5, 5))
# Expected output: 3

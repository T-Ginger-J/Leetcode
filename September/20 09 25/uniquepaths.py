# LeetCode 62: Unique Paths
# Explanation:
# 1. Use DP table where dp[i][j] = number of ways to reach cell (i,j).
# 2. Transition: dp[i][j] = dp[i-1][j] + dp[i][j-1].
# 3. Base case: first row and first column = 1.
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1]*n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


# Example usage:
# sol = Solution()
# print(sol.uniquePaths(3, 7))  # 28
# print(sol.uniquePaths(3, 2))  # 3

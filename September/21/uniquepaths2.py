# LeetCode 63: Unique Paths II
# Explanation:
# 1. Use DP table where dp[i][j] = number of ways to reach (i,j).
# 2. If obstacleGrid[i][j] == 1, dp[i][j] = 0.
# 3. Otherwise, dp[i][j] = dp[i-1][j] + dp[i][j-1].
# 4. Base case: dp[0][0] = 1 if no obstacle.
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0]*n for _ in range(m)]
        
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                elif i > 0 or j > 0:
                    dp[i][j] = (dp[i-1][j] if i > 0 else 0) + (dp[i][j-1] if j > 0 else 0)
        
        return dp[-1][-1]

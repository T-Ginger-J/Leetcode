// LeetCode 63: Unique Paths II
// Explanation:
// 1. Use DP table where dp[i][j] = number of paths to reach (i,j).
// 2. If obstacleGrid[i][j] == 1, dp[i][j] = 0.
// 3. Otherwise, dp[i][j] = dp[i-1][j] + dp[i][j-1].
// Time Complexity: O(m*n)
// Space Complexity: O(m*n)

public class Solution {
    public int UniquePathsWithObstacles(int[][] obstacleGrid) {
        int m = obstacleGrid.Length, n = obstacleGrid[0].Length;
        int[,] dp = new int[m, n];
        
        dp[0,0] = obstacleGrid[0][0] == 0 ? 1 : 0;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (obstacleGrid[i][j] == 1) {
                    dp[i,j] = 0;
                } else if (i > 0 || j > 0) {
                    int fromTop = i > 0 ? dp[i-1,j] : 0;
                    int fromLeft = j > 0 ? dp[i,j-1] : 0;
                    dp[i,j] += fromTop + fromLeft;
                }
            }
        }
        return dp[m-1,n-1];
    }
}


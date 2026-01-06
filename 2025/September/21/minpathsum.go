// LeetCode 64: Minimum Path Sum
// Explanation:
// 1. Use DP table where dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j].
// 2. Initialize first row and column with cumulative sums.
// Time Complexity: O(m*n)
// Space Complexity: O(m*n)

func minPathSum(grid [][]int) int {
    m, n := len(grid), len(grid[0])
    dp := make([][]int, m)
    for i := range dp {
        dp[i] = make([]int, n)
    }
    dp[0][0] = grid[0][0]
    for i := 1; i < m; i++ {
        dp[i][0] = dp[i-1][0] + grid[i][0]
    }
    for j := 1; j < n; j++ {
        dp[0][j] = dp[0][j-1] + grid[0][j]
    }
    for i := 1; i < m; i++ {
        for j := 1; j < n; j++ {
            if dp[i-1][j] < dp[i][j-1] {
                dp[i][j] = dp[i-1][j] + grid[i][j]
            } else {
                dp[i][j] = dp[i][j-1] + grid[i][j]
            }
        }
    }
    return dp[m-1][n-1]
}

// Example usage:
// fmt.Println(minPathSum([][]int{{1,3,1},{1,5,1},{4,2,1}})) // 7
// fmt.Println(minPathSum([][]int{{1,2,3},{4,5,6}}))         // 12

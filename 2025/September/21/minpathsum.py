# LeetCode 64: Minimum Path Sum
# Explanation:
# 1. Use DP: dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j].
# 2. Base case: first row and first column accumulate sums.
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0]*n for _ in range(m)]
        dp[0][0] = grid[0][0]
        
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
        
        return dp[-1][-1]
    
    def minPathSum1D(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [float('inf')] * n
        dp[0] = 0
        for i in range(m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j-1]) + grid[i][j]
        return dp[-1]
    
    minPathSumOneLine=lambda s,g:((m:=len(g)) and (n:=len(g[0])) and (dp:=[10**9]*n) and (dp.__setitem__(0,0) or [dp.__setitem__(0,dp[0]+g[i][0]) or [dp.__setitem__(j,min(dp[j],dp[j-1])+g[i][j]) for j in range(1,n)] for i in range(m)]) and dp[-1])

# Example usage:
# sol = Solution()
# print(sol.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))  # 7
# print(sol.minPathSum([[1,2,3],[4,5,6]]))          # 12

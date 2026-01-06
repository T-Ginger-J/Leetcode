# LeetCode 329: Longest Increasing Path in a Matrix
# Explanation:
# 1. The path can move up, down, left, or right.
# 2. Use DFS + memoization (DP) to store the longest path starting at each cell.
# 3. For each cell, explore neighbors with strictly larger values.
# 4. Memoize results so each cell's DFS is computed once.
#
# Time Complexity: O(m * n)
# Space Complexity: O(m * n) for memo + recursion stack

class Solution:
    def longestIncreasingPath(self, matrix):
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]  # memo table
        
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        def dfs(i, j):
            if dp[i][j] != 0:
                return dp[i][j]
            
            best = 1  # Each cell is a path of length 1
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and matrix[ni][nj] > matrix[i][j]:
                    best = max(best, 1 + dfs(ni, nj))
            
            dp[i][j] = best
            return best
        
        longest = 1
        for i in range(m):
            for j in range(n):
                longest = max(longest, dfs(i, j))
        
        return longest

# Example 1
# Input:
matrix = [
    [9,9,4],
    [6,6,8],
    [2,1,1]
]
# Output: 4
# Explanation: Longest path: 1 → 2 → 6 → 9

print(Solution().longestIncreasingPath(matrix))  # Output: 4

# Example 2
matrix = [
    [3,4,5],
    [3,2,6],
    [2,2,1]
]
# Output: 4 (3 → 4 → 5 → 6)
print(Solution().longestIncreasingPath(matrix))  # Output: 4

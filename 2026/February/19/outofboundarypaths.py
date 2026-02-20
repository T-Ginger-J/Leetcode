# LeetCode 576: Out of Boundary Paths
# Explanation:
# 1. Given an m x n grid, a ball starts at (i,j) and can move in four directions.
# 2. Task: Find the number of paths that move the ball out of boundary in at most N moves.
# 3. Approach:
#    - Use dynamic programming: dp[k][r][c] = number of ways to move out of boundary in k moves from (r,c)
#    - Recurrence: dp[k][r][c] = sum of dp[k-1][nr][nc] for all four directions; increment count if next move goes out of boundary.
#    - Use memoization to optimize recursion.
# 4. Time Complexity: O(m * n * N)
# 5. Space Complexity: O(m * n * N) for memoization

from functools import lru_cache

class Solution:

    # -------------------------------------------------------
    # Method 1: DFS + memoization
    # -------------------------------------------------------
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        MOD = 10**9 + 7
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]

        @lru_cache(None)
        def dfs(x, y, moves):
            if x < 0 or x >= m or y < 0 or y >= n:
                return 1
            if moves == 0:
                return 0
            total = 0
            for dx, dy in dirs:
                total = (total + dfs(x+dx, y+dy, moves-1)) % MOD
            return total

        return dfs(i,j,N)

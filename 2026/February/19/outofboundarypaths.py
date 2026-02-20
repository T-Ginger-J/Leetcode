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

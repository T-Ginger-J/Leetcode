# LeetCode 200: Number of Islands
# Explanation:
# 1. Traverse grid; when '1' found, increment count and DFS to mark all connected '1's as '0'.
# 2. Each DFS call explores up, down, left, right.
# Time Complexity: O(m * n)
# Space Complexity: O(m * n) for recursion stack in worst case.

class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    dfs(r, c)
        return count

    def numIslandsBFS(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        islands = 0

        def bfs(r, c):
            q = deque([(r, c)])
            grid[r][c] = '0'
            while q:
                x, y = q.popleft()
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1':
                        grid[nx][ny] = '0'
                        q.append((nx, ny))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    islands += 1
                    bfs(r, c)
        return islands

    def numIslandsOneLine(self, g): return sum(__import__('itertools').starmap(lambda i,j:(f:=lambda x,y:x in range(len(g))and y in range(len(g[0]))and g[x][y]=='1'and[g.__setitem__(x,g[x][:y]+'0'+g[x][y+1:]),[f(x+1,y),f(x-1,y),f(x,y+1),f(x,y-1)]][1])(i,j),[(i,j)for i in range(len(g))for j in range(len(g[0]))if g[i][j]=='1'])))


sol = Solution()
print(sol.numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))  # 3

print(sol.numIslands([
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]))  # 1


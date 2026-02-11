# LeetCode 542: 01 Matrix
# Explanation:
# 1. Given a matrix with 0s and 1s, update each cell with the distance to the nearest 0.
# 2. Distance is measured in number of steps (Manhattan distance).
# 3. Use BFS starting from all 0s simultaneously to fill distances.

# Methods Used:
# - Multi-source BFS (Optimal)
# - Alternative: DP pass (top-left & bottom-right)

# Time Complexity:
# - O(m*n), m = rows, n = cols

# Space Complexity:
# - O(m*n) for BFS queue


from typing import List
from collections import deque


class Solution:

    # -------------------------------------------------------
    # Method 1: BFS from All Zeros
    # -------------------------------------------------------
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:

        if not mat:
            return []

        m, n = len(mat), len(mat[0])
        dist = [[float('inf')] * n for _ in range(m)]
        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i,j))

        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if dist[nx][ny] > dist[x][y] + 1:
                        dist[nx][ny] = dist[x][y] + 1
                        queue.append((nx, ny))

        return dist


# -------------------------------------------------------
# Examples (Including Edge Cases)
# -------------------------------------------------------

# Example 1
mat1 = [[0,0,0],[0,1,0],[0,0,0]]
print(Solution().updateMatrix(mat1))
# [[0,0,0],[0,1,0],[0,0,0]]

# Example 2
mat2 = [[0,0,0],[0,1,0],[1,1,1]]
print(Solution().updateMatrix(mat2))
# [[0,0,0],[0,1,0],[1,2,1]]

# Example 3 (All zeros)
mat3 = [[0,0],[0,0]]
print(Solution().updateMatrix(mat3))
# [[0,0],[0,0]]

# Example 4 (All ones with single zero)
mat4 = [[1,1,1],[1,0,1],[1,1,1]]
print(Solution().updateMatrix(mat4))
# [[2,1,2],[1,0,1],[2,1,2]]

# Example 5 (Empty matrix)
mat5 = []
print(Solution().updateMatrix(mat5))
# []

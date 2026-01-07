# LeetCode 407: Trapping Rain Water II
# Explanation:
# 1. Use priority queue with all boundary cells
# 2. Pop lowest height, update neighbors
# 3. Water trapped = max(0, height_boundary - neighbor_height)
# Time Complexity: O(m*n log(m*n))
# Space Complexity: O(m*n)

import heapq

class Solution:
    def trapRainWater(self, heightMap: list[list[int]]) -> int:
        if not heightMap or not heightMap[0]: return 0
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False]*n for _ in range(m)]
        heap = []

        # push boundary cells into heap
        for i in range(m):
            for j in [0, n-1]:
                heapq.heappush(heap, (heightMap[i][j], i, j))
                visited[i][j] = True
        for j in range(n):
            for i in [0, m-1]:
                if not visited[i][j]:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True

        water = 0
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        while heap:
            h, x, y = heapq.heappop(heap)
            for dx, dy in dirs:
                nx, ny = x+dx, y+dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    water += max(0, h - heightMap[nx][ny])
                    heapq.heappush(heap, (max(heightMap[nx][ny], h), nx, ny))
                    visited[nx][ny] = True
        return water


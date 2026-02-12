# LeetCode 547: Number of Provinces
# Explanation:
# 1. Given an n x n adjacency matrix isConnected where isConnected[i][j] = 1 if city i and city j are directly connected.
# 2. A province is a group of directly or indirectly connected cities.
# 3. Count number of connected components in the graph.

# Methods Used:
# - DFS or BFS to traverse connected cities
# - Alternative: Union-Find

# Time Complexity:
# - O(n^2), since adjacency matrix size is n x n

# Space Complexity:
# - O(n) for visited array or union-find parent array


from typing import List


class Solution:

    # -------------------------------------------------------
    # Method 1: DFS
    # -------------------------------------------------------
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        visited = [False] * n

        def dfs(city):
            visited[city] = True
            for j in range(n):
                if isConnected[city][j] == 1 and not visited[j]:
                    dfs(j)

        provinces = 0
        for i in range(n):
            if not visited[i]:
                provinces += 1
                dfs(i)

        return provinces


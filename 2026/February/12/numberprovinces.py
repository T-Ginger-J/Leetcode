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

    # -------------------------------------------------------
    # Method 2: Union-Find
    # -------------------------------------------------------
    def findCircleNumUF(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    union(i, j)

        return sum(1 for i in range(n) if parent[i] == i)


# -------------------------------------------------------
# Examples (Including Edge Cases)
# -------------------------------------------------------

# Example 1
isConnected1 = [[1,1,0],[1,1,0],[0,0,1]]
print(Solution().findCircleNum(isConnected1))  # 2

# Example 2
isConnected2 = [[1,0,0],[0,1,0],[0,0,1]]
print(Solution().findCircleNum(isConnected2))  # 3

# Example 3 (All connected)
isConnected3 = [[1,1,1],[1,1,1],[1,1,1]]
print(Solution().findCircleNum(isConnected3))  # 1

# Example 4 (Empty matrix)
isConnected4 = []
print(Solution().findCircleNum(isConnected4))  # 0

# Example 5 (Single city)
isConnected5 = [[1]]
print(Solution().findCircleNum(isConnected5))  # 1

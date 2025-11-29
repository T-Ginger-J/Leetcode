# LeetCode 310: Minimum Height Trees
# Explanation:
# 1. Use BFS to remove leaf nodes iteratively.
# 2. The last remaining nodes are the roots of minimum height trees.
# 3. Build an adjacency list, track leaves, remove them layer by layer.
# Time Complexity: O(n), each edge and node processed once
# Space Complexity: O(n), adjacency list and leaves

from collections import deque, defaultdict

class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1: return [0]
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)

        leaves = deque([i for i in range(n) if len(graph[i]) == 1])

        while n > 2:
            n -= len(leaves)
            new_leaves = deque()
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves

        return list(leaves)

sol = Solution()
print(sol.findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))  # [1]
print(sol.findMinHeightTrees(6, [[0,3],[1,3],[2,3],[4,3],[5,4]]))  # [3,4]
print(sol.findMinHeightTrees(1, []))  # [0]

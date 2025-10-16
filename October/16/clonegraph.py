# LeetCode 133: Clone Graph
# Explanation:
# 1. Each node has neighbors, forming an undirected graph.
# 2. We use DFS or BFS to clone every node and its neighbors.
# 3. Maintain a hashmap mapping original nodes to cloned ones to prevent duplicates.
# Time Complexity: O(V + E), where V = number of nodes, E = number of edges.
# Space Complexity: O(V)

from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        old_to_new = {}

        def dfs(n):
            if n in old_to_new:
                return old_to_new[n]
            clone = Node(n.val)
            old_to_new[n] = clone
            for nei in n.neighbors:
                clone.neighbors.append(dfs(nei))
            return clone

        return dfs(node)

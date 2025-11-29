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

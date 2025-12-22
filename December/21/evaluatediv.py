# LeetCode 399: Evaluate Division
# Explanation:
# 1. Build a graph of variables and division values
# 2. DFS to evaluate each query
# Time Complexity: O(Q * N)
# Space Complexity: O(N + E)

from collections import defaultdict

class Solution:
    def calcEquation(self, equations, values, queries):
        graph = defaultdict(dict)
        for (A, B), val in zip(equations, values):
            graph[A][B] = val
            graph[B][A] = 1 / val

        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            visited.add(start)
            for neighbor, val in graph[start].items():
                if neighbor in visited:
                    continue
                product = dfs(neighbor, end, visited)
                if product != -1.0:
                    return val * product
            return -1.0

        results = []
        for X, Y in queries:
            results.append(dfs(X, Y, set()))
        return results

equations = [["a","b"], ["b","c"]]
values = [2.0, 3.0]
queries = [["a","c"], ["b","a"], ["a","e"], ["a","a"], ["x","x"]]

print(Solution().calcEquation(equations, values, queries))
# Output: [6.0, 0.5, -1.0, 1.0, -1.0]

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


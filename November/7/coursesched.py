# LeetCode 207: Course Schedule
# Explanation:
# 1. Build graph adjacency list and in-degree count.
# 2. Start with nodes (courses) having in-degree 0.
# 3. Remove edges iteratively while updating in-degrees.
# 4. If all nodes processed, return True (no cycle).
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)

from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        visited = 0

        while queue:
            course = queue.popleft()
            visited += 1
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return visited == numCourses
    

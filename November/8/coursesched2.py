# LeetCode 210: Course Schedule II
# Explanation:
# 1. Build adjacency list and in-degree count.
# 2. Start with nodes having in-degree 0 (no prerequisites).
# 3. Pop from queue, reduce in-degrees of dependent courses.
# 4. If all courses processed → return order; else empty list.
# Time Complexity: O(V + E)
# Space Complexity: O(V + E)

from collections import *

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph = defaultdict(list)
        indegree = [0] * numCourses
        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)
            for nxt in graph[course]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)

        return order if len(order) == numCourses else []

    def findOrderOneLine(self,n,p):g=defaultdict(list);[g[b].append(a)for a,b in p];r=[];v=[0]*n;f=lambda c:not(v[c]==1 or(v[c]==0 and any(not f(x)for x in g[c]))or(r.append(c),v.__setitem__(c,2)));return []if any(not f(i)for i in range(n))else r[::-1]


sol = Solution()
print(sol.findOrder(2, [[1,0]]))                  # [0,1]
print(sol.findOrder(4, [[1,0],[2,0],[3,1],[3,2]]))# [0,1,2,3] or [0,2,1,3]
print(sol.findOrder(1, []))                       # [0]

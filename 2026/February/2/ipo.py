from typing import List
import heapq

class Solution:
    def findMaximizedCapital(self, k: int, W: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))
        max_heap = []
        i = 0
        n = len(projects)

        for _ in range(k):
            while i < n and projects[i][0] <= W:
                heapq.heappush(max_heap, -projects[i][1])
                i += 1
            if not max_heap:
                break
            W += -heapq.heappop(max_heap)
        return W


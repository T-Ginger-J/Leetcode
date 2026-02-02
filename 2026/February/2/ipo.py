# LeetCode 502: IPO
# Explanation:
# Given k projects, each with a profit and a required capital,
# choose at most k projects to maximize final capital W.
#
# Method 1: Greedy + Heaps (Optimal)
# - Sort projects by required capital.
# - Use a max-heap to store profits of projects whose capital requirement <= current W.
# - Repeatedly select the most profitable available project.
#
# Time Complexity: O(n log n)
# Space Complexity: O(n)

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


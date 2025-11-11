# LeetCode 218: The Skyline Problem
# Explanation:
# 1. Use a sweep line algorithm.
# 2. Treat building edges as events: (x, height, start/end).
# 3. Use max heap to track current active building heights.
# 4. When current max height changes, add a key point to result.
# Time Complexity: O(n log n)
# Space Complexity: O(n)

import heapq
from collections import Counter

class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        events = []
        for l, r, h in buildings:
            events.append((l, -h, r))  # start of building
            events.append((r, 0, 0))   # end marker
        events.sort()

        res = [[0, 0]]
        heap = [(0, float('inf'))]

        for x, neg_h, r in events:
            while heap and heap[0][1] <= x:
                heapq.heappop(heap)
            if neg_h:
                heapq.heappush(heap, (neg_h, r))
            curr_h = -heap[0][0]
            if res[-1][1] != curr_h:
                res.append([x, curr_h])
        return res[1:]

    def getSkylineLazy(self, buildings: list[list[int]]) -> list[list[int]]:
        events = []
        for l, r, h in buildings:
            events.append((l, -h))
            events.append((r, h))
        events.sort()

        res, heap, removed = [], [0], Counter()
        prev = 0
        for x, h in events:
            if h < 0:
                heapq.heappush(heap, h)
            else:
                removed[-h] += 1
            while heap and removed[-heap[0]]:
                removed[-heap[0]] -= 1
                heapq.heappop(heap)
            curr = -heap[0]
            if curr != prev:
                res.append([x, curr])
                prev = curr
        return res

sol = Solution()
print(sol.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
# [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

print(sol.getSkyline([[0,2,3],[2,5,3]]))
# [[0,3],[5,0]]

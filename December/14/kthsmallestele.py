# LeetCode 378: Kth Smallest Element in a Sorted Matrix
# Explanation:
# 1. Use min-heap to track next smallest element.
# 2. Push next element in the same row after popping.
# Time Complexity: O(k log n)
# Space Complexity: O(n)

import heapq

class Solution:
    def kthSmallest(self, matrix, k: int) -> int:
        n = len(matrix)
        heap = []
        for i in range(min(k, n)):
            heapq.heappush(heap, (matrix[i][0], i, 0))
        count = 0
        while heap:
            val, r, c = heapq.heappop(heap)
            count += 1
            if count == k:
                return val
            if c + 1 < n:
                heapq.heappush(heap, (matrix[r][c+1], r, c+1))

matrix = [
    [1,5,9],
    [10,11,13],
    [12,13,15]
]
k = 8
print(Solution().kthSmallest(matrix, k))  # Output: 13

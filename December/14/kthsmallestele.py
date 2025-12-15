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

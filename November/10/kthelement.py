# LeetCode 215: Kth Largest Element in an Array
# Explanation:
# 1. Maintain a min heap of size k.
# 2. For each element, push into heap and pop smallest if heap grows too large.
# 3. The top of the heap is the kth largest.
# Time Complexity: O(n log k)
# Space Complexity: O(k)

import heapq
import random

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap, n)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

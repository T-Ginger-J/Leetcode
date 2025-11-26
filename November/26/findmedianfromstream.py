# LeetCode 295: Find Median from Data Stream
# Explanation:
# 1. Use two heaps to maintain the lower half (max heap) and upper half (min heap) of numbers.
# 2. max_heap stores negative numbers to simulate a max heap in Python.
# 3. On insertion:
#    - Add to appropriate heap.
#    - Rebalance heaps so that their sizes differ at most by 1.
# 4. Median:
#    - If even number of elements, median = average of tops of both heaps.
#    - If odd, median = top of the heap with more elements.
# Time Complexity:
#   - addNum: O(log n)
#   - findMedian: O(1)
# Space Complexity: O(n), storing all numbers

import heapq

class MedianFinder:

    def __init__(self):
        self.max_heap = []  # left half (max heap)
        self.min_heap = []  # right half (min heap)

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        # ensure every element in max_heap <= every element in min_heap
        if self.max_heap and self.min_heap and (-self.max_heap[0] > self.min_heap[0]):
            val = -heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, val)
        # rebalance heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        else:
            return (-self.max_heap[0] + self.min_heap[0]) / 2


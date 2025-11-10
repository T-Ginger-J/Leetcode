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

    def findKthLargestQuickselect(self, nums: list[int], k: int) -> int:
        k = len(nums) - k
        def quickselect(l, r):
            pivot = nums[random.randint(l, r)]
            i, j = l, r
            while i <= j:
                while nums[i] < pivot: i += 1
                while nums[j] > pivot: j -= 1
                if i <= j:
                    nums[i], nums[j] = nums[j], nums[i]
                    i, j = i + 1, j - 1
            if k <= j: return quickselect(l, j)
            if k >= i: return quickselect(i, r)
            return nums[k]
        return quickselect(0, len(nums) - 1)

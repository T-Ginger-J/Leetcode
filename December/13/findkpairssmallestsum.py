# LeetCode 373: Find K Pairs with Smallest Sums
# Explanation:
# 1. Initialize min-heap with (nums1[i]+nums2[0], i, 0)
# 2. Pop smallest sum, push next element in nums2.
# Time Complexity: O(k log k)
# Space Complexity: O(k)

import heapq

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        if not nums1 or not nums2:
            return []
        heap = []
        res = []
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i]+nums2[0], i, 0))
        while heap and len(res) < k:
            s, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            if j + 1 < len(nums2):
                heapq.heappush(heap, (nums1[i]+nums2[j+1], i, j+1))
        return res

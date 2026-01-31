# LeetCode 496: Next Greater Element I
# Explanation:
# Given two arrays nums1 and nums2, find the next greater element of each
# element in nums1 within nums2.
#
# Method 1: Monotonic Stack + Hash Map (Optimal)
# - Iterate nums2 and use a stack to keep track of decreasing elements.
# - When a larger element appears, pop from stack and record next greater.
# - Lookup for nums1 in the hashmap for results.
#
# Time Complexity: O(n + m), n = len(nums1), m = len(nums2)
# Space Complexity: O(m)

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)
        # Remaining elements have no next greater
        for num in stack:
            next_greater[num] = -1
        return [next_greater[num] for num in nums1]


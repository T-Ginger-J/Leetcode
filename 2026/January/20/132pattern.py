# LeetCode 456: 132 Pattern
# Explanation:
# Given an array nums, determine if there exists a 132 pattern:
# i < j < k such that nums[i] < nums[k] < nums[j].
#
# Method 1: Monotonic Stack (Optimal)
# - Traverse from right to left.
# - Maintain a decreasing stack for potential "3" values.
# - Keep track of the best candidate for "2".
# - If we find a value smaller than "2", a 132 pattern exists.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        second = float('-inf')

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < second:
                return True
            while stack and nums[i] > stack[-1]:
                second = stack.pop()
            stack.append(nums[i])

        return False

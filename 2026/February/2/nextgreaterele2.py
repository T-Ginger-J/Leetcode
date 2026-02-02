# LeetCode 503: Next Greater Element II
# Explanation:
# Given a circular array nums, find the next greater number for each element.
# The next greater number is the first greater number traversing forward,
# wrapping around if necessary.
#
# Method 1: Monotonic Stack with Circular Traversal (Optimal)
# - Traverse the array twice (2 * n) to simulate circular behavior.
# - Use a decreasing stack storing indices.
# - Fill result when a greater element is found.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [-1] * n
        stack = []

        for i in range(2 * n):
            while stack and nums[stack[-1]] < nums[i % n]:
                res[stack.pop()] = nums[i % n]
            if i < n:
                stack.append(i)
        return res


# Alternate Python Solution: Brute Force (Educational)
# - For each element, scan forward up to n steps.
# - Useful for understanding but not optimal.

class SolutionBrute:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            found = -1
            for j in range(1, n + 1):
                if nums[(i + j) % n] > nums[i]:
                    found = nums[(i + j) % n]
                    break
            res.append(found)
        return res

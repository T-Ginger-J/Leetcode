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


# Additional Examples (Edge Cases and Non-LeetCode Examples)

sol = Solution()

# Example 1: Circular needed
print(sol.nextGreaterElements([1,2,1]))
# Expected output: [2,-1,2]

# Example 2: All equal elements
print(sol.nextGreaterElements([3,3,3]))
# Expected output: [-1,-1,-1]

# Example 3: Strictly decreasing
print(sol.nextGreaterElements([5,4,3,2,1]))
# Expected output: [-1,5,5,5,5]

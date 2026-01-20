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


# Additional Examples (Edge Cases and Non-LeetCode Examples)

sol = Solution()

# Example 1: Simple 132 pattern
print(sol.find132pattern([3,1,4,2]))
# Expected output: True (1,4,2)

# Example 2: Strictly increasing
print(sol.find132pattern([1,2,3,4]))
# Expected output: False

# Example 3: Pattern with negative numbers
print(sol.find132pattern([-1,3,2,0]))
# Expected output: True

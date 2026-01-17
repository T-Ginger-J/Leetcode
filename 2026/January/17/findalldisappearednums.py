# LeetCode 448: Find All Numbers Disappeared in an Array
# Explanation:
# Given an array nums of n integers where 1 ≤ nums[i] ≤ n, some elements may be missing.
# Goal: return all numbers in the range [1, n] that do NOT appear in nums.
#
# Method 1: In-Place Negative Marking (Optimal)
# - Iterate through nums:
#     1. For each number nums[i], map it to index abs(nums[i]) - 1.
#     2. Negate the value at that index to mark it as seen.
# - After marking, any index with positive value corresponds to a missing number.
#
# Time Complexity: O(n)
# Space Complexity: O(1) (ignoring output list)

from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])
        return [i + 1 for i, num in enumerate(nums) if num > 0]

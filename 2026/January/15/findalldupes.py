# LeetCode 442: Find All Duplicates in an Array
# Explanation:
# Given an array nums of n integers where 1 ≤ nums[i] ≤ n, some elements appear twice.
# Goal: return all elements that appear twice without using extra space.
#
# Method 1: In-Place Negative Marking (Optimal)
# - For each number nums[i], map it to index abs(nums[i]) - 1.
# - Negate the value at that index to mark it as seen.
# - If the value is already negative, the number is a duplicate.
#
# Time Complexity: O(n)
# Space Complexity: O(1) (ignoring output list)

from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            if nums[index] < 0:
                res.append(abs(nums[i]))
            else:
                nums[index] = -nums[index]
        return res

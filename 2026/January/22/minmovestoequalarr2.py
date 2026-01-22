# LeetCode 462: Minimum Moves to Equal Array Elements II
# Explanation:
# Given an integer array nums, find the minimum number of moves required
# to make all elements equal. One move increments or decrements an element by 1.
#
# Key Insight:
# - The optimal target value is the median of the array.
# - Minimizing sum(|nums[i] - x|) occurs when x is the median.
#
# Method 1: Sort + Median (Optimal)
# - Sort the array.
# - Choose the middle element as the median.
# - Sum absolute differences to the median.
#
# Time Complexity: O(n log n)
# Space Complexity: O(1) (ignoring sort)

from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        median = nums[len(nums) // 2]
        return sum(abs(x - median) for x in nums)

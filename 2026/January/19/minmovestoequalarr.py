# LeetCode 453: Minimum Moves to Equal Array Elements
# Explanation:
# Given an integer array nums, in one move you can increment n - 1 elements by 1.
# Find the minimum number of moves to make all elements equal.
#
# Key Insight:
# - Incrementing n-1 elements by 1 is equivalent to decrementing 1 element by 1.
# - Therefore, the goal becomes reducing all elements down to the minimum value.
#
# Method 1: Mathematical Reduction (Optimal)
# - Let min_val be the minimum element in nums.
# - Each element nums[i] needs (nums[i] - min_val) decrements.
# - Total moves = sum(nums) - min_val * n
#
# Time Complexity: O(n)
# Space Complexity: O(1)
#
# Method 2: Sorting-Based (Alternative, clearer intuition)
# - Sort the array.
# - Accumulate differences between elements and the smallest value.
#
# Time Complexity: O(n log n)
# Space Complexity: O(1) or O(n) depending on sort implementation

from typing import List

class Solution:
    # Method 1: Math (Optimal)
    def minMoves(self, nums: List[int]) -> int:
        min_val = min(nums)
        return sum(nums) - min_val * len(nums)

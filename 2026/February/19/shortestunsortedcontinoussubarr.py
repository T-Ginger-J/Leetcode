# LeetCode 581: Shortest Unsorted Continuous Subarray
# Explanation:
# 1. Given an integer array, find the shortest continuous subarray that, if sorted, results in the entire array being sorted.
# 2. Approach:
#    - Method 1: Sort a copy of the array and compare with original to find leftmost and rightmost mismatch.
#    - Method 2 (optimized): Scan from left to right to find the max so far and mark right boundary where current < max. Scan from right to left to find min so far and mark left boundary where current > min.
# 3. Time Complexity: 
#    - Method 1: O(n log n)
#    - Method 2: O(n)
# 4. Space Complexity:
#    - Method 1: O(n)
#    - Method 2: O(1)

from typing import List

class Solution:

    # -------------------------------------------------------
    # Method 1: Sorting
    # -------------------------------------------------------
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        left, right = 0, len(nums)-1
        while left < len(nums) and nums[left] == sorted_nums[left]:
            left += 1
        while right >= 0 and nums[right] == sorted_nums[right]:
            right -= 1
        return 0 if left > right else right - left + 1


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


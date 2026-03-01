from typing import List
import bisect


class Solution:

    # Main Solution: Two Pointers
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0

        for i in range(n - 1, 1, -1):
            left = 0
            right = i - 1

            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1

        return count


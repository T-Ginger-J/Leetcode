# LeetCode 75: Sort Colors
# Explanation:
# 1. Count number of 0s, 1s, and 2s.
# 2. Overwrite nums array with correct counts.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        count0 = count1 = count2 = 0
        for num in nums:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1

        for i in range(count0):
            nums[i] = 0
        for i in range(count0, count0 + count1):
            nums[i] = 1
        for i in range(count0 + count1, len(nums)):
            nums[i] = 2

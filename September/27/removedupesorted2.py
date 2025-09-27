# LeetCode 80: Remove Duplicates from Sorted Array II
# Explanation:
# 1. Use two-pointer technique.
# 2. Keep writing elements to position k if it's valid (<=2 duplicates).
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 0
        for num in nums:
            if k < 2 or num != nums[k-2]:
                nums[k] = num
                k += 1
        return k

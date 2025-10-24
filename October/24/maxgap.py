# LeetCode 164: Maximum Gap
# Explanation:
# 1. Given an unsorted array, find the maximum difference between successive elements in sorted form.
# 2. Sorting directly and finding max diff works in O(n log n).
# 3. Sort nums, then compute max(nums[i+1] - nums[i]).
# Time Complexity: O(n log n)
# Space Complexity: O(1) or O(n) depending on sorting algorithm

class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        nums.sort()
        return max(nums[i+1] - nums[i] for i in range(len(nums) - 1))

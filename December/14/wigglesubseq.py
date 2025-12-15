# LeetCode 376: Wiggle Subsequence
# Explanation:
# 1. Track up and down differences.
# 2. Count alternations between positive and negative differences.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def wiggleMaxLength(self, nums):
        if not nums:
            return 0
        up = down = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up = down + 1
            elif nums[i] < nums[i-1]:
                down = up + 1
        return max(up, down)

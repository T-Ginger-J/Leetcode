# LeetCode 238: Product of Array Except Self
# Explanation:
# Build output array as prefix products.
# Then multiply each position by its suffix product computed on the fly.
#
# Steps:
# 1. output[i] = product of nums[0..i-1]
# 2. Traverse from right with suffix = product of nums[i+1..end]
#    output[i] *= suffix
#
# Time Complexity: O(n)
# Space Complexity: O(1) extra (output array allowed by LC)

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n

        # prefix
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # suffix
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res

# LeetCode 152: Maximum Product Subarray
# Explanation:
# 1. Keep track of both the current maximum and minimum products at each index.
# 2. Negative numbers can flip max and min, so we swap when encountering them.
# 3. Update global maximum with current maximum.
# 4. This dynamic programming approach handles positive, negative, and zero values.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def maxProduct(self, nums):
        cur_max = cur_min = res = nums[0]
        for n in nums[1:]:
            if n < 0:
                cur_max, cur_min = cur_min, cur_max
            cur_max = max(n, cur_max * n)
            cur_min = min(n, cur_min * n)
            res = max(res, cur_max)
        return res


from itertools import accumulate

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        best = curr = nums[0]
        for n in nums[1:]:
            curr = max(n, curr + n)
            best = max(best, curr)
        return best

    def maxSubArrayOptimized(self, nums: list[int]) -> int:
        max_sum = float('-inf')
        curr = 0
        for n in nums:
            curr = n + (curr if curr > 0 else 0)
            if curr > max_sum:
                max_sum = curr
        return max_sum

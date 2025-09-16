from itertools import accumulate

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        best = curr = nums[0]
        for n in nums[1:]:
            curr = max(n, curr + n)
            best = max(best, curr)
        return best


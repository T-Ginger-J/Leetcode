from typing import List
from functools import lru_cache

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return nums[i]
            pick_i = nums[i] - dp(i + 1, j)
            pick_j = nums[j] - dp(i, j - 1)
            return max(pick_i, pick_j)

        return dp(0, n - 1) >= 0


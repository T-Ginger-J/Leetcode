from typing import List
from functools import lru_cache

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        @lru_cache(None)
        def dfs(i, total):
            if i == len(nums):
                return 1 if total == S else 0
            return dfs(i+1, total + nums[i]) + dfs(i+1, total - nums[i])
        
        return dfs(0, 0)


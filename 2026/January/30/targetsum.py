# LeetCode 494: Target Sum
# Explanation:
# Given an integer array nums and a target S, count the number of ways
# to assign '+' or '-' to each element such that the sum equals S.
#
# Method 1: DFS + Memoization
# - Use recursion to try adding and subtracting each number.
# - Memoize results with (index, current_sum) as key.
#
# Time Complexity: O(n * sum(nums))
# Space Complexity: O(n * sum(nums))

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


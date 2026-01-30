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


# Alternate Python Solution: Dynamic Programming (Subset Sum Transformation)
# - Transform problem into finding subsets with sum = (S + sum(nums)) / 2
# - Classic 0/1 knapsack problem

class SolutionDP:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        total = sum(nums)
        if (S + total) % 2 != 0 or S > total:
            return 0
        target = (S + total) // 2
        dp = [0] * (target + 1)
        dp[0] = 1
        for num in nums:
            for t in range(target, num - 1, -1):
                dp[t] += dp[t - num]
        return dp[target]


# Additional Examples (Edge Cases and Non-LeetCode Examples)

sol = Solution()

# Example 1: Simple case
print(sol.findTargetSumWays([1,1,1,1,1], 3))
# Expected output: 5

# Example 2: Single element
print(sol.findTargetSumWays([1], 1))
# Expected output: 1

# Example 3: Impossible target
print(sol.findTargetSumWays([1,2,3], 7))
# Expected output: 0

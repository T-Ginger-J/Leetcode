# LeetCode 377: Combination Sum IV
# Explanation:
# 1. dp[i] = sum(dp[i - num] for num in nums if i >= num)
# 2. dp[0] = 1
# Time Complexity: O(target * len(nums))
# Space Complexity: O(target)

class Solution:
    def combinationSum4(self, nums, target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, target + 1):
            for num in nums:
                if i >= num:
                    dp[i] += dp[i - num]
        return dp[target]

print(Solution().combinationSum4([1,2,3], 4))  # Output: 7
# Combinations: [1,1,1,1],[1,1,2],[1,2,1],[2,1,1],[2,2],[1,3],[3,1]

print(Solution().combinationSum4([9], 3))      # Output: 0

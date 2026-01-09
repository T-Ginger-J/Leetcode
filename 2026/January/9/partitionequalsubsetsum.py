# LeetCode 416: Partition Equal Subset Sum
# Explanation:
# 1. If total sum is odd, cannot partition
# 2. Use DP to check if subset sum = total/2 exists
# Time Complexity: O(n*sum/2)
# Space Complexity: O(sum/2)

class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(target, num-1, -1):
                dp[i] = dp[i] or dp[i-num]
        return dp[target]


# LeetCode 312: Burst Balloons
# Explanation:
# 1. Use DP with the idea of last balloon to burst in a subarray.
# 2. nums = [1] + original + [1] to simplify boundaries.
# 3. dp[i][j] = max coins from bursting balloons between i and j (exclusive).
# 4. dp[i][j] = max(dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j]) for i<k<j
# Time Complexity: O(n^3)
# Space Complexity: O(n^2)

class Solution:
    def maxCoins(self, nums):
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        for length in range(2, n):
            for left in range(0, n-length):
                right = left + length
                for k in range(left+1, right):
                    dp[left][right] = max(dp[left][right], dp[left][k]+dp[k][right]+nums[left]*nums[k]*nums[right])
        return dp[0][n-1]

    def maxCoinsMemoization(self, nums):
        nums = [1]+nums+[1]
        n = len(nums)
        memo = [[0]*n for _ in range(n)]
        
        def dp(left, right):
            if left+1 == right:
                return 0
            if memo[left][right] != 0:
                return memo[left][right]
            memo[left][right] = max(dp(left,k)+dp(k,right)+nums[left]*nums[k]*nums[right] for k in range(left+1,right))
            return memo[left][right]
        
        return dp(0,n-1)

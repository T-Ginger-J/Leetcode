# LeetCode 368: Largest Divisible Subset
# Explanation:
# 1. Sort nums to ensure divisible property only needs to check previous numbers.
# 2. Use dp[i] to store largest subset size ending at i.
# 3. Use prev[i] to reconstruct the subset.
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def largestDivisibleSubset(self, nums):
        if not nums:
            return []
        nums.sort()
        n = len(nums)
        dp = [1] * n
        prev = [-1] * n
        max_idx = 0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
            if dp[i] > dp[max_idx]:
                max_idx = i

        res = []
        while max_idx != -1:
            res.append(nums[max_idx])
            max_idx = prev[max_idx]
        return res[::-1]  # reverse to get increasing order


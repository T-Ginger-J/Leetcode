# LeetCode 198: House Robber
# Explanation:
# 1. Use dynamic programming: dp[i] = max money robbed up to i-th house.
# 2. For each house i, choose max of:
#       - rob current (nums[i] + dp[i-2])
#       - skip current (dp[i-1])
# 3. Return dp[-1].
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]
    
    def robSpaceOptimized(self, nums: list[int]) -> int:
        prev1 = prev2 = 0
        for n in nums:
            prev1, prev2 = max(prev1, prev2 + n), prev1
        return prev1
    
    def rob(self, nums: list[int]) -> int: return __import__('functools').reduce(lambda a,x:(max(a[0],a[1]+x),a[0]),nums,(0,0))[0]

sol = Solution()
print(sol.rob([1,2,3,1]))   # 4
print(sol.rob([2,7,9,3,1])) # 12

class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        nums.sort()
        return max(nums[i+1] - nums[i] for i in range(len(nums) - 1))

class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        n = len(nums)
        sum_nums = sum(nums)
        F = sum(i * num for i, num in enumerate(nums))
        max_val = F
        for i in range(n-1, 0, -1):
            F = F + sum_nums - n * nums[i]
            max_val = max(max_val, F)
        return max_val

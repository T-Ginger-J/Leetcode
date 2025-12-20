# LeetCode 396: Rotate Function
# Explanation:
# 1. Compute F(0) and total sum
# 2. Use F(k+1) = F(k) + sum - n * nums[n-k-1]
# 3. Track max value
# Time Complexity: O(n)
# Space Complexity: O(1)

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

print(Solution().maxRotateFunction([4,3,2,6]))  # Output: 26
print(Solution().maxRotateFunction([1,2,3,4,5])) # Output: 40

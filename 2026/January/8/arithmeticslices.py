# LeetCode 413: Arithmetic Slices
# Explanation:
# 1. dp[i] = number of slices ending at i
# 2. If nums[i]-nums[i-1] == nums[i-1]-nums[i-2], extend previous slices
# Time Complexity: O(n)
# Space Complexity: O(1) (optimized)

class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        total = 0
        current = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                current += 1
                total += current
            else:
                current = 0
        return total

nums = [1,2,3,4]
print(Solution().numberOfArithmeticSlices(nums))  # Output: 3

nums = [1,3,5,7,9]
print(Solution().numberOfArithmeticSlices(nums))  # Output: 6

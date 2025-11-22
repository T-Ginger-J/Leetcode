# LeetCode 273: Integer to English Words
# LeetCode 268: Missing Number
# Explanation:
# 1. Use the sum formula for 0..n and subtract the sum of array elements to find missing number.
# 2. This works because sum(0..n) = n*(n+1)//2.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)
    
# Example usage:
# sol = Solution()
# print(sol.missingNumber([3,0,1]))  # 2
# print(sol.missingNumber([0,1]))    # 2
# print(sol.missingNumber([9,6,4,2,3,5,7,0,1]))  # 8

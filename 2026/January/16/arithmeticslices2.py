# LeetCode 446: Arithmetic Slices II - Subsequence
# Explanation:
# Given an integer array nums, count the number of **arithmetic subsequences** of length >= 3.
# - A subsequence can be non-contiguous.
# - An arithmetic subsequence has a constant difference between consecutive elements.
#
# Method 1: Dynamic Programming with Hashmaps (Optimal)
# - For each index i, keep a hashmap dp[i] mapping:
#     difference -> count of subsequences ending at i with this difference (length >= 2)
# - For each pair (i, j) with j < i:
#     - diff = nums[i] - nums[j]
#     - If dp[j] has sequences with this diff, extend them by nums[i]
#     - Update dp[i][diff] accordingly
# - Only count sequences of length >= 3 (subtract sequences of length 2)
#
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

from typing import List
from collections import defaultdict

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        total = 0
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                count = dp[j][diff]
                dp[i][diff] += count + 1
                total += count  # Only subsequences of length >= 3 are counted
        
        return total

# Additional Examples (Edge Cases and Non-LeetCode Examples)

sol = Solution()

# Example 1: Simple arithmetic sequence
nums1 = [2,4,6,8,10]
print(sol.numberOfArithmeticSlices(nums1))  
# Expected output: 7
# (subsequences: [2,4,6], [4,6,8], [6,8,10], [2,4,6,8], [4,6,8,10], [2,4,6,8,10], [2,6,10])

# Example 2: No arithmetic subsequences
nums2 = [1,2,4]
print(sol.numberOfArithmeticSlices(nums2))  
# Expected output: 0

# Example 3: Negative differences
nums3 = [7,4,1,-2]
print(sol.numberOfArithmeticSlices(nums3))  
# Expected output: 3
# ([7,4,1], [4,1,-2], [7,4,1,-2])

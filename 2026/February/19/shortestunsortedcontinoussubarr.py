# LeetCode 581: Shortest Unsorted Continuous Subarray
# Explanation:
# 1. Given an integer array, find the shortest continuous subarray that, if sorted, results in the entire array being sorted.
# 2. Approach:
#    - Method 1: Sort a copy of the array and compare with original to find leftmost and rightmost mismatch.
#    - Method 2 (optimized): Scan from left to right to find the max so far and mark right boundary where current < max. Scan from right to left to find min so far and mark left boundary where current > min.
# 3. Time Complexity: 
#    - Method 1: O(n log n)
#    - Method 2: O(n)
# 4. Space Complexity:
#    - Method 1: O(n)
#    - Method 2: O(1)

from typing import List

class Solution:

    # -------------------------------------------------------
    # Method 1: Sorting
    # -------------------------------------------------------
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        left, right = 0, len(nums)-1
        while left < len(nums) and nums[left] == sorted_nums[left]:
            left += 1
        while right >= 0 and nums[right] == sorted_nums[right]:
            right -= 1
        return 0 if left > right else right - left + 1

    # -------------------------------------------------------
    # Method 2: One-pass without extra space
    # -------------------------------------------------------
    def findUnsortedSubarrayOptimized(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, -1
        max_seen = float('-inf')
        min_seen = float('inf')

        for i in range(n):
            max_seen = max(max_seen, nums[i])
            if nums[i] < max_seen:
                right = i

        for i in range(n-1, -1, -1):
            min_seen = min(min_seen, nums[i])
            if nums[i] > min_seen:
                left = i

        return 0 if right == -1 else right - left + 1


# -------------------------------------------------------
# Examples & Edge Cases
# -------------------------------------------------------

sol = Solution()

# Example 1
nums1 = [2,6,4,8,10,9,15]
print(sol.findUnsortedSubarray(nums1))                 # 5 ([6,4,8,10,9])
print(sol.findUnsortedSubarrayOptimized(nums1))        # 5

# Example 2: already sorted
nums2 = [1,2,3,4]
print(sol.findUnsortedSubarray(nums2))                 # 0

# Example 3: reverse sorted
nums3 = [5,4,3,2,1]
print(sol.findUnsortedSubarray(nums3))                 # 5

# Example 4: single element
nums4 = [1]
print(sol.findUnsortedSubarray(nums4))                 # 0

# Example 5: two elements swapped
nums5 = [1,3,2,4,5]
print(sol.findUnsortedSubarrayOptimized(nums5))        # 2 ([3,2])

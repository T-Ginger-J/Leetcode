# LeetCode 153: Find Minimum in Rotated Sorted Array
# Explanation:
# 1. Use binary search to locate the minimum element.
# 2. Compare middle element with rightmost element to decide which side is unsorted.
# 3. If nums[mid] > nums[right], min must be to the right.
# 4. Otherwise, it’s on the left (including mid).
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]

print(Solution().findMin([3,4,5,1,2]))
# Output: 1

print(Solution().findMin([4,5,6,7,0,1,2]))
# Output: 0

print(Solution().findMin([11,13,15,17]))
# Output: 11

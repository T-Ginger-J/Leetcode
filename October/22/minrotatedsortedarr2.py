# LeetCode 154: Find Minimum in Rotated Sorted Array II
# Explanation:
# 1. Similar to LeetCode 153, but this version allows duplicates.
# 2. When nums[mid] == nums[right], we can’t decide which side to go, so we shrink the search space by right -= 1.
# 3. Otherwise, apply the same binary search logic as before.
# 4. Continue until left == right, where the minimum resides.
# Time Complexity: O(log n) average, O(n) worst (due to duplicates)
# Space Complexity: O(1)

class Solution:
    def findMin(self, nums):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] < nums[right]:
                right = mid
            else:
                right -= 1
        return nums[left]

print(Solution().findMin([1,3,5]))
# Output: 1

print(Solution().findMin([2,2,2,0,1]))
# Output: 0

print(Solution().findMin([10,10,10,1,10]))
# Output: 1

# LeetCode 283: Move Zeroes
# Explanation:
# 1. We need to move all 0's to the end while maintaining the relative order of non-zero elements.
# 2. Use a slow pointer to track the position to insert the next non-zero element.
# 3. Traverse the array with a fast pointer:
#    - If nums[fast] != 0, place it at nums[slow] and increment slow.
# 4. After traversal, fill the remaining positions with 0.
# Time Complexity: O(n)
# Space Complexity: O(1), in-place

class Solution:
    def moveZeroes(self, nums):
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        return nums


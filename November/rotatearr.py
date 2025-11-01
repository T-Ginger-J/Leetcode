# LeetCode 189: Rotate Array
# Explanation:
# 1. To rotate array right by k steps, we can reverse parts of the array:
#    - Reverse the entire array
#    - Reverse the first k elements
#    - Reverse the remaining elements
# 2. This achieves the rotation in-place without extra space.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

    def rotateSlicing(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

    def rotateOneLine(self, nums: list[int], k: int) -> None: nums[:] = nums[-(k%len(nums)):] + nums[:-(k%len(nums))]

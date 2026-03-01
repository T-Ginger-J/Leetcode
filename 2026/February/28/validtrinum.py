# LeetCode 611: Valid Triangle Number
# Explanation:
# 1. Given an array nums of non-negative integers, count how many triplets
#    (i, j, k) can form a triangle.
# 2. Three sides form a valid triangle if:
#    a + b > c (when a <= b <= c).
# 3. Sort the array first.
# 4. Fix the largest side c, then use two pointers to find pairs (a, b)
#    such that a + b > c.
# 5. If nums[left] + nums[right] > nums[i], then all elements between
#    left and right form valid triangles with nums[i].
#
# Method 1 (Two Pointers After Sorting):
# - Sort nums.
# - Iterate i from n-1 to 2.
# - Use left/right pointers for remaining two sides.
#
# Time Complexity: O(n^2)
# Space Complexity: O(1) (excluding sort)
#
# Alternative Method 1 (Binary Search):
# - Fix two sides i, j.
# - Binary search largest k where nums[i] + nums[j] > nums[k].
# - Slower in practice.
#
# Alternative Method 2 (Brute Force - Educational):
# - Check all triplets.
# - O(n^3), not optimal, only for understanding.


from typing import List
import bisect


class Solution:

    # Main Solution: Two Pointers
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0

        for i in range(n - 1, 1, -1):
            left = 0
            right = i - 1

            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += right - left
                    right -= 1
                else:
                    left += 1

        return count


    # Alternative Solution 1: Binary Search
    def triangleNumberAlt1(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        count = 0

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                target = nums[i] + nums[j]
                k = bisect.bisect_left(nums, target, j + 1)
                count += max(0, k - j - 1)

        return count


    # Alternative Solution 2: Brute Force (Not Optimal)
    def triangleNumberAlt2(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    a, b, c = nums[i], nums[j], nums[k]
                    if a + b > c and a + c > b and b + c > a:
                        count += 1

        return count


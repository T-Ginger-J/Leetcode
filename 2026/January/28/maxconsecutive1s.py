# LeetCode 485: Max Consecutive Ones
# Explanation:
# Given a binary array, return the maximum number of consecutive 1s.
#
# Method 1: Linear Scan (Optimal)
# - Traverse the array keeping a current count of consecutive 1s.
# - Update the maximum whenever a 0 is encountered.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0
        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0
        return max_count


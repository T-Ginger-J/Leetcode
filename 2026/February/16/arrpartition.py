# LeetCode 561: Array Partition I
# Explanation:
# 1. Given an array of 2n integers, group these integers into n pairs (a, b) such that sum of min(a, b) for all pairs is maximized.
# 2. Approach:
#    - To maximize the sum of minimums, sort the array.
#    - Pair consecutive elements; sum every first element of each pair.
# 3. Time Complexity: O(n log n) for sorting
# 4. Space Complexity: O(1) or O(n) depending on sorting implementation

from typing import List

class Solution:

    # -------------------------------------------------------
    # Method 1: Sort and sum every other element
    # -------------------------------------------------------
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])


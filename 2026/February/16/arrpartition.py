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

    # -------------------------------------------------------
    # Method 2: Counting sort optimization (for known value range)
    # -------------------------------------------------------
    def arrayPairSumCounting(self, nums: List[int]) -> int:
        offset = 10000  # nums[i] range: [-10000,10000]
        count = [0]*20001
        for num in nums:
            count[num + offset] += 1
        sum_min = 0
        take = True
        for i in range(20001):
            while count[i] > 0:
                if take:
                    sum_min += i - offset
                take = not take
                count[i] -= 1
        return sum_min

# LeetCode 477: Total Hamming Distance
# Explanation:
# Given an integer array nums, return the sum of Hamming distances
# between all pairs of the integers.
#
# Key Insight:
# - Hamming distance depends on differing bits.
# - For each bit position (0..31), count how many numbers have bit=1.
# - If count = ones, zeros = n - ones
# - Contribution = ones * zeros
#
# Method 1: Bit Counting (Optimal)
#
# Time Complexity: O(32 * n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)

        for bit in range(32):
            ones = 0
            for num in nums:
                ones += (num >> bit) & 1
            total += ones * (n - ones)

        return total


# Alternate Python Solution: Built-in Bit Operations
# - Iterate bits until max bit length.
# - Slightly cleaner for smaller inputs.

class SolutionBitLength:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        max_bits = max(nums).bit_length()

        for bit in range(max_bits):
            ones = sum((num >> bit) & 1 for num in nums)
            total += ones * (n - ones)

        return total

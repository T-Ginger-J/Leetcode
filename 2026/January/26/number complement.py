# LeetCode 476: Number Complement
# Explanation:
# Given a positive integer num, return its complement.
# The complement flips all bits in the binary representation of num,
# ignoring leading zeros.
#
# Method 1: Bitmask Construction (Optimal)
# - Create a mask with all bits set to 1 up to the highest bit of num.
# - XOR num with the mask to flip only relevant bits.
#
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def findComplement(self, num: int) -> int:
        mask = 1
        while mask <= num:
            mask <<= 1
        return (mask - 1) ^ num


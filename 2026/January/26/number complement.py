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


# Alternate Python Solution: Using bit_length()
# - bit_length gives number of bits needed to represent num.
# - Build mask directly using (1 << bit_length) - 1

class SolutionBitLength:
    def findComplement(self, num: int) -> int:
        return ((1 << num.bit_length()) - 1) ^ num


# Additional Examples (Edge Cases and Non-LeetCode Examples)

sol = Solution()

# Example 1: Single bit
print(sol.findComplement(1))
# Expected output: 0

# Example 2: Power of two
print(sol.findComplement(8))
# Expected output: 7

# Example 3: Mixed bits
print(sol.findComplement(21))
# Expected output: 10

# LeetCode 190: Reverse Bits
# Explanation:
# 1. Iterate through all 32 bits of the input integer.
# 2. For each bit, shift the result left and add the current bit (n & 1).
# 3. Shift n right to process the next bit.
# 4. Return the reversed integer.
# Time Complexity: O(1) (constant 32-bit loop)
# Space Complexity: O(1)

class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>= 1
        return result

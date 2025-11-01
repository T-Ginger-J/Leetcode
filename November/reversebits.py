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

    def reverseBitsManip(self, n: int) -> int:
        n = ((n >> 1) & 0x55555555) | ((n & 0x55555555) << 1)
        n = ((n >> 2) & 0x33333333) | ((n & 0x33333333) << 2)
        n = ((n >> 4) & 0x0f0f0f0f) | ((n & 0x0f0f0f0f) << 4)
        n = ((n >> 8) & 0x00ff00ff) | ((n & 0x00ff00ff) << 8)
        n = ((n >> 16) & 0x0000ffff) | ((n & 0x0000ffff) << 16)
        return n

    def reverseBits(self, n: int) -> int: return int(f"{n:032b}"[::-1], 2)

sol = Solution()
print(sol.reverseBits(0b00000010100101000001111010011100))  # 964176192
print(sol.reverseBits(0b11111111111111111111111111111101))  # 3221225471
print(sol.reverseBits(0))                                   # 0

# LeetCode 191: Number of 1 Bits
# Explanation:
# 1. Count how many bits are set to 1 in the binary representation of n.
# 2. Keep checking the last bit using n & 1, then right shift n.
# 3. Continue until n becomes 0.
# Time Complexity: O(1)  (since there are always 32 bits)
# Space Complexity: O(1)

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            count += n & 1
            n >>= 1
        return count

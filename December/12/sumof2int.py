# LeetCode 371: Sum of Two Integers
# Explanation:
# 1. Use XOR for sum without carry.
# 2. AND + shift for carry.
# 3. Repeat until carry is zero.
# Time Complexity: O(1) (max 32 iterations)
# Space Complexity: O(1)

class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK
        # handle negative numbers
        return a if a <= 0x7FFFFFFF else ~(a ^ MASK)

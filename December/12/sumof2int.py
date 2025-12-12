class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & MASK
            b = carry & MASK
        # handle negative numbers
        return a if a <= 0x7FFFFFFF else ~(a ^ MASK)

# LeetCode 405: Convert a Number to Hexadecimal
# Explanation:
# 1. Handle negative numbers with two's complement
# 2. Mask last 4 bits repeatedly
# 3. Map to hex characters
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        hex_chars = "0123456789abcdef"
        # handle negative numbers
        num &= 0xFFFFFFFF
        res = ""
        while num:
            res = hex_chars[num & 0xf] + res
            num >>= 4
        return res

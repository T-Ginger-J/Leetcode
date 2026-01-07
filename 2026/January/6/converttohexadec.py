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

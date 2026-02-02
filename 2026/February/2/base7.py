class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        neg = num < 0
        num = abs(num)
        digits = []

        while num > 0:
            digits.append(str(num % 7))
            num //= 7

        res = "".join(reversed(digits))
        return "-" + res if neg else res

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        res = 10  # n = 1
        product = 9
        for i in range(2, n+1):
            product *= (11 - i)
            res += product
        return res

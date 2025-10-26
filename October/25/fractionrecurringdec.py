# LeetCode 166: Fraction to Recurring Decimal
# Explanation:
# 1. Divide numerator by denominator to get integer part.
# 2. For remainder, multiply by 10 and divide again to get decimal digits.
# 3. Use a hashmap to store each remainder’s index in the result — if a remainder repeats, that means we’ve found the repeating cycle.
# 4. Handle sign and edge cases (negative fractions, division by 0).
# Time Complexity: O(n) where n is the number of digits before repetition.
# Space Complexity: O(n) for storing remainders and result digits.

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        res = []
        if (numerator < 0) ^ (denominator < 0):
            res.append('-')

        numerator, denominator = abs(numerator), abs(denominator)
        res.append(str(numerator // denominator))
        remainder = numerator % denominator
        if remainder == 0:
            return ''.join(res)

        res.append('.')
        remainders = {}
        while remainder:
            if remainder in remainders:
                res.insert(remainders[remainder], '(')
                res.append(')')
                break
            remainders[remainder] = len(res)
            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator

        return ''.join(res)

    def fractionToDecimalOneLine(self, n, d):
        return "0" if not n else ("-" if (n<0)^(d<0) else "") + (lambda n,d,r,s:(lambda f:f(f,n%d,n//d,s))(lambda f,r,q,s:s+str(q) if not r else (s+"."+f(f,r*10,0,{r:len(s)+1}))) if not r else s+str(n//d))(abs(n),abs(d),0,"")


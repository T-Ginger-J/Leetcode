import math


class Solution:

    # -------------------------------------------------------
    # Method 1: Iterative Parsing (Main Solution)
    # -------------------------------------------------------
    def fractionAddition(self, expression: str) -> str:

        i = 0
        n = len(expression)

        num = 0   # current numerator
        den = 1   # current denominator

        while i < n:

            # Handle sign
            sign = 1
            if expression[i] == "+":
                i += 1
            elif expression[i] == "-":
                sign = -1
                i += 1

            # Read numerator
            curr_num = 0
            while i < n and expression[i].isdigit():
                curr_num = curr_num * 10 + int(expression[i])
                i += 1

            curr_num *= sign

            # Skip '/'
            i += 1

            # Read denominator
            curr_den = 0
            while i < n and expression[i].isdigit():
                curr_den = curr_den * 10 + int(expression[i])
                i += 1

            # Add fractions
            num = num * curr_den + curr_num * den
            den = den * curr_den

            # Reduce
            g = math.gcd(abs(num), den)
            num //= g
            den //= g

        return f"{num}/{den}"


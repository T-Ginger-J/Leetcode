# LeetCode 592: Fraction Addition and Subtraction
# Explanation:
# 1. We are given a string expression containing fractions with '+' and '-' operators.
#    Example: "-1/2+1/2+1/3"
# 2. We need to compute the result and return it in simplest form.
# 3. Approach:
#    - Parse the expression term by term.
#    - Keep a running numerator and denominator.
#    - For each fraction a/b:
#        new_num = cur_num * b + a * cur_den
#        new_den = cur_den * b
#    - Reduce by GCD after each addition.
# 4. Use math.gcd to simplify.
# 5. Time Complexity: O(n), n = length of expression
# 6. Space Complexity: O(1), only variables used

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

    # -------------------------------------------------------
    # Method 2: Using Python Fractions (Alternative)
    # -------------------------------------------------------
    def fractionAdditionUsingLibrary(self, expression: str) -> str:

        from fractions import Fraction

        i = 0
        n = len(expression)
        result = Fraction(0, 1)

        while i < n:

            sign = 1
            if expression[i] == "+":
                i += 1
            elif expression[i] == "-":
                sign = -1
                i += 1

            # numerator
            num = 0
            while i < n and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1

            num *= sign
            i += 1  # skip '/'

            # denominator
            den = 0
            while i < n and expression[i].isdigit():
                den = den * 10 + int(expression[i])
                i += 1

            result += Fraction(num, den)

        return f"{result.numerator}/{result.denominator}"


# -------------------------------------------------------
# Examples & Edge Cases
# -------------------------------------------------------

sol = Solution()

# Example 1: Basic addition
expr1 = "-1/2+1/2"
print(sol.fractionAddition(expr1))   # 0/1

# Example 2: Multiple operations
expr2 = "-1/2+1/2+1/3"
print(sol.fractionAddition(expr2))   # 1/3

# Example 3: Negative result
expr3 = "1/3-1/2"
print(sol.fractionAddition(expr3))   # -1/6

# Example 4: Large numbers
expr4 = "5/3+1/3"
print(sol.fractionAddition(expr4))   # 2/1

# Example 5: Single fraction
expr5 = "-7/4"
print(sol.fractionAddition(expr5))   # -7/4

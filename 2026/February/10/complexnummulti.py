# LeetCode 537: Complex Number Multiplication
# Explanation:
# 1. Complex numbers are given as strings "a+bi".
# 2. To multiply (a+bi)*(c+di), use formula:
#    real = a*c - b*d
#    imag = a*d + b*c
# 3. Return result in "x+yi" format.

# Methods Used:
# - String Parsing
# - Arithmetic Multiplication

# Time Complexity:
# - O(1), strings are short

# Space Complexity:
# - O(1)


class Solution:

    # -------------------------------------------------------
    # Method 1: Parse and Multiply (Optimal)
    # -------------------------------------------------------
    def complexNumberMultiply(self, a: str, b: str) -> str:

        def parse(s):
            real, imag = s.split('+')
            return int(real), int(imag[:-1])

        a_real, a_imag = parse(a)
        b_real, b_imag = parse(b)

        real = a_real * b_real - a_imag * b_imag
        imag = a_real * b_imag + a_imag * b_real

        return f"{real}+{imag}i"

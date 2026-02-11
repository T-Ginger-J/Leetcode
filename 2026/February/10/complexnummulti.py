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


# -------------------------------------------------------
# Examples (Including Edge Cases)
# -------------------------------------------------------

# Example 1
a1, b1 = "1+1i", "1+1i"
print(Solution().complexNumberMultiply(a1, b1))  # "0+2i"

# Example 2
a2, b2 = "1+-1i", "1+-1i"
print(Solution().complexNumberMultiply(a2, b2))  # "0+-2i"

# Example 3 (Zero multiplication)
a3, b3 = "0+0i", "3+4i"
print(Solution().complexNumberMultiply(a3, b3))  # "0+0i"

# Example 4 (Negative numbers)
a4, b4 = "-1+-1i", "1+-1i"
print(Solution().complexNumberMultiply(a4, b4))  # "0+2i"

# Example 5 (Large numbers)
a5, b5 = "123+456i", "789+987i"
print(Solution().complexNumberMultiply(a5, b5))  # "-357345+1011153i"

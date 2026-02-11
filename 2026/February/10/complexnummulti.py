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

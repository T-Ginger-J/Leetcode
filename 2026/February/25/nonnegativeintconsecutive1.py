class Solution:

    def findIntegers(self, n: int) -> int:

        # Convert n to binary as a list of bits
        bits = []
        x = n
        while x:
            bits.append(x & 1)
            x >>= 1
        bits = bits[::-1]  # MSB first

        L = len(bits)

        # Precompute fib[i]
        fib = [0] * (L + 2)
        fib[0] = 1
        fib[1] = 2
        for i in range(2, L+1):
            fib[i] = fib[i-1] + fib[i-2]

        ans = 0
        prev_bit = 0
        for i, b in enumerate(bits):
            if b == 1:
                ans += fib[L - i - 1]
                if prev_bit == 1:
                    return ans
                prev_bit = 1
            else:
                prev_bit = 0

        return ans + 1  # Include n itself if valid


# LeetCode 600: Non-negative Integers without Consecutive Ones
# Explanation:
# 1. Given a number n, count all non-negative integers <= n
#    whose binary representation does NOT contain consecutive 1's.
# 2. Approach (Dynamic Programming + Bit Manipulation):
#    - Let fib[i] = number of valid binary strings of length i
#      without consecutive 1's.
#    - fib[i] = fib[i-1] + fib[i-2] (similar to Fibonacci)
#    - Convert n to binary, traverse from MSB to LSB
#      and count valid numbers smaller than n.
#    - Stop if consecutive 1's appear.
# 3. Time Complexity: O(log n)
# 4. Space Complexity: O(log n) for binary representation

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


# -------------------------------------------------------
# Examples & Edge Cases
# -------------------------------------------------------

sol = Solution()

# Example 1
print(sol.findIntegers(5))   # 5 (0,1,2,4,5)

# Example 2
print(sol.findIntegers(1))   # 2 (0,1)

# Example 3
print(sol.findIntegers(2))   # 3 (0,1,2)

# Example 4: Larger number
print(sol.findIntegers(20))  # 13

# Example 5: Consecutive 1s edge
print(sol.findIntegers(3))   # 3 (0,1,2)

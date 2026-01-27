# LeetCode 479: Largest Palindrome Product
# Explanation:
# Given an integer n, return the largest palindrome made from the product
# of two n-digit numbers. Since the result can be large, return it modulo 1337.
#
# Key Insight:
# - The largest palindrome is likely formed by large numbers.
# - Instead of brute forcing all products, generate palindromes directly
#   from the first half and check if they can be factored into two n-digit numbers.
#
# Method 1: Palindrome Construction + Factor Check (Optimal)
# - Iterate left half from largest to smallest.
# - Construct palindrome by mirroring.
# - Check if palindrome can be factored into two n-digit numbers.
#
# Time Complexity: O(10^n) in practice much faster due to early stopping
# Space Complexity: O(1)

class Solution:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9

        upper = 10**n - 1
        lower = 10**(n - 1)

        for left in range(upper, lower - 1, -1):
            pal = int(str(left) + str(left)[::-1])
            for x in range(upper, int(pal ** 0.5) - 1, -1):
                if pal % x == 0:
                    y = pal // x
                    if lower <= y <= upper:
                        return pal % 1337
        return 0


# Alternate Python Solution: Early Pruning with Divisibility
# - Same palindrome generation
# - Skip factor checks when divisor too small early

class SolutionOptimized:
    def largestPalindrome(self, n: int) -> int:
        if n == 1:
            return 9

        upper = 10**n - 1
        lower = 10**(n - 1)

        for left in range(upper, lower - 1, -1):
            pal = int(str(left) + str(left)[::-1])
            for x in range(upper, lower - 1, -1):
                if x * x < pal:
                    break
                if pal % x == 0:
                    return pal % 1337
        return 0



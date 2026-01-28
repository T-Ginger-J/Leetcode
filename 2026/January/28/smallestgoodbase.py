# LeetCode 483: Smallest Good Base
# Explanation:
# Given a number n as a string, find the smallest good base k such that
# n can be written as 1 + k + k^2 + ... + k^m for some m >= 1.
#
# Key Insight:
# - For a given length m+1 of the representation, k satisfies:
#     n = (k^(m+1) - 1) / (k - 1)
# - Try m from largest possible (floor(log2(n))) down to 1.
# - Solve for integer k using binary search.
#
# Time Complexity: O(log n * log n)
# Space Complexity: O(1)

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        max_m = n.bit_length() - 1  # maximum length of representation

        for m in range(max_m, 1, -1):
            left, right = 2, int(n ** (1/m)) + 1
            while left <= right:
                k = (left + right) // 2
                s = (k ** (m + 1) - 1) // (k - 1)
                if s == n:
                    return str(k)
                elif s < n:
                    left = k + 1
                else:
                    right = k - 1

        return str(n - 1)  # default base for 1+1+...+1 representation


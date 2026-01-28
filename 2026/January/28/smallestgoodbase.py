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


# Alternate Python Solution: Direct Formula for k
# - Use floating point approximation for k, round and check integer solution.

class SolutionApprox:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        max_m = n.bit_length() - 1

        for m in range(max_m, 1, -1):
            k = int(n ** (1/m))
            if (k ** (m + 1) - 1) // (k - 1) == n:
                return str(k)

        return str(n - 1)


# Additional Examples (Edge Cases and Non-LeetCode Examples)

sol = Solution()

# Example 1: Small number
print(sol.smallestGoodBase("13"))
# Expected output: "3"  (13 = 1 + 3 + 9)

# Example 2: Power of 2
print(sol.smallestGoodBase("31"))
# Expected output: "2"  (31 = 1 + 2 + 4 + 8 + 16)

# Example 3: Prime number
print(sol.smallestGoodBase("17"))
# Expected output: "16" (17 = 1 + 16)

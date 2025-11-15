# LeetCode 231: Power of Two
# Explanation:
# A positive number n is a power of two if it has exactly one '1' in its binary form.
# This means: n & (n - 1) == 0  (and n must be > 0)
#
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0

# Example usage:
# sol = Solution()
# print(sol.isPowerOfTwo(1))   # True
# print(sol.isPowerOfTwo(16))  # True
# print(sol.isPowerOfTwo(18))  # False
# print(sol.isPowerOfTwo(1024))   # True
# print(sol.isPowerOfTwo(12))     # False

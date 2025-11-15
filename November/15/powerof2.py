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


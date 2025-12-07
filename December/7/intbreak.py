# LeetCode 343: Integer Break
# Explanation:
# 1. Keep breaking n into 3's because they produce the highest product.
# 2. If leftover is 4, use 2 * 2 instead of 3 + 1.
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def integerBreak(self, n):
        if n <= 3:
            return n - 1

        res = 1
        while n > 4:
            res *= 3
            n -= 3
        return res * n

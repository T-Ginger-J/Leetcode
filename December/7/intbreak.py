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

    def integerBreakDP(self, n):
        dp = [0] * (n + 1)
        dp[1] = 1

        for i in range(2, n + 1):
            for j in range(1, i):
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]

print(Solution().integerBreak(2))  # Output: 1
print(Solution().integerBreak(10)) # Output: 36  (3+3+4 → 3*3*4)

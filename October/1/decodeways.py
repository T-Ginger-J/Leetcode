# LeetCode 91: Decode Ways
# Explanation:
# 1. Each digit or pair of digits ("1" to "26") can represent a letter (A-Z).
# 2. Use dynamic programming:
#    - dp[i] = number of ways to decode up to index i.
#    - Single digit valid if 1 <= s[i] <= 9.
#    - Two digits valid if 10 <= s[i-1:i+1] <= 26.
# 3. dp[n] gives total decoding ways.
# Time Complexity: O(n)
# Space Complexity: O(n) (can be optimized to O(1))

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        n = len(s)
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, n + 1):
            one = int(s[i-1])
            two = int(s[i-2:i])
            if 1 <= one <= 9:
                dp[i] += dp[i-1]
            if 10 <= two <= 26:
                dp[i] += dp[i-2]
        return dp[n]

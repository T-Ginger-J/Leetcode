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

from functools import lru_cache

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

    def numDecodingsOptimized(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        prev, curr = 1, 1
        for i in range(1, len(s)):
            temp = 0
            if s[i] != "0":
                temp += curr
            if 10 <= int(s[i-1:i+1]) <= 26:
                temp += prev
            prev, curr = curr, temp
        return curr
    
    def numDecodings(self, s: str) -> int:
        return (f:=lru_cache(None)(lambda i: 1 if i==len(s) else 0 if s[i]=="0" else f(i+1)+(f(i+2) if i+1<=len(s)-1 and 10<=int(s[i:i+2])<=26 else 0)))(0)

# Example 1
print(Solution().numDecodings("12"))  # 2 ("AB", "L")

# Example 2
print(Solution().numDecodings("226"))  # 3 ("BZ", "VF", "BBF")

# Example 3
print(Solution().numDecodings("06"))  # 0


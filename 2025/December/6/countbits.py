# LeetCode 338: Counting Bits
# Explanation:
# 1. Use DP: bits[i] = bits[i >> 1] + (i & 1)
# 2. Right shift removes LSB; (i & 1) adds if LSB was 1.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def countBits(self, n):
        dp = [0] * (n + 1)
        for i in range(1, n + 1):
            dp[i] = dp[i >> 1] + (i & 1)
        return dp

    def countBitsBuiltIn(self, n):
        return [bin(i).count("1") for i in range(n + 1)]

print(Solution().countBits(5))
# Output: [0,1,1,2,1,2]

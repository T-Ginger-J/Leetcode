# LeetCode 279: Perfect Squares
# Explanation:
# 1. We want the minimum number of perfect squares that sum to n.
# 2. Use dynamic programming (DP) where dp[i] = min number of squares summing to i.
# 3. Initialize dp[0] = 0.
# 4. For each number i from 1 to n:
#    - Try all squares j*j <= i.
#    - dp[i] = min(dp[i], dp[i - j*j] + 1)
# 5. dp[n] will give the answer.
# Time Complexity: O(n * sqrt(n)) because for each i we try sqrt(i) squares.
# Space Complexity: O(n) for the dp array.

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j*j] + 1)
                j += 1
        return dp[n]

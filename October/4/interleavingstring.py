# LeetCode 97: Interleaving String
# Explanation:
# 1. We need to determine if s3 can be formed by interleaving s1 and s2.
# 2. Interleaving means preserving the order of characters in both s1 and s2.
# 3. Use DP where dp[i][j] = True if s3[:i+j] can be formed by s1[:i] and s2[:j].
# 4. Transition:
#    dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[i+j-1]) or (dp[i][j-1] and s2[j-1]==s3[i+j-1])
# 5. Base Case: dp[0][0] = True
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        m, n = len(s1), len(s2)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or \
                           (dp[i][j-1] and s2[j-1] == s3[i+j-1])

        return dp[m][n]

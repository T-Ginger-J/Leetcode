class Solution:
    def isMatch(self, s, p):
        m, n = len(s), len(p)
        
        # dp[i][j] means s[:i] matches p[:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # Handle patterns like a*, a*b*, a*b*c* matching empty string
        for j in range(2, n + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] != '*':
                    dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
                else:
                    # Case 1: '*' = zero occurrences
                    dp[i][j] = dp[i][j - 2]
                    # Case 2: '*' = one or more occurrences
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        dp[i][j] |= dp[i - 1][j]

        return dp[m][n]
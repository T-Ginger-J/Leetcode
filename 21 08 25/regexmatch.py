class Solution:
    def isMatchDP(self, s, p):
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
    
    def isMatchDFS(self, s, p):
        memo = {}
        
        def dfs(i, j):
            # If already computed
            if (i, j) in memo:
                return memo[(i, j)]
            
            # If pattern is consumed, string must also be consumed
            if j == len(p):
                return i == len(s)
            
            # First match condition
            first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            
            if j + 1 < len(p) and p[j + 1] == '*':
                # Case 1: skip x*
                # Case 2: use x* (if first matches)
                ans = dfs(i, j + 2) or (first_match and dfs(i + 1, j))
            else:
                ans = first_match and dfs(i + 1, j + 1)
            
            memo[(i, j)] = ans
            return ans
        
        return dfs(0, 0)

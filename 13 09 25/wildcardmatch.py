#O(n)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True

        # Handle patterns starting with *
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == "?" or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == "*":
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

        return dp[m][n]
    
    
    def isMatchGreedy(self, s: str, p: str) -> bool:
        i = j = 0  # pointers for s and p
        star_idx = -1
        match = 0

        while i < len(s):
            if j < len(p) and (p[j] == s[i] or p[j] == "?"):
                i += 1
                j += 1
            elif j < len(p) and p[j] == "*":
                star_idx = j
                match = i
                j += 1
            elif star_idx != -1:
                j = star_idx + 1
                match += 1
                i = match
            else:
                return False

        while j < len(p) and p[j] == "*":
            j += 1

        return j == len(p)


sol = Solution()
print(sol.isMatch("aa", "a"))      # False
print(sol.isMatch("aa", "*"))      # True
print(sol.isMatch("cb", "?a"))     # False
print(sol.isMatch("adceb", "*a*b"))# True
print(sol.isMatch("acdcb", "a*c?b")) # False

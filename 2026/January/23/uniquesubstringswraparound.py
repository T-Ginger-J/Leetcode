class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        dp = [0] * 26
        curr_len = 0

        for i in range(len(p)):
            if i > 0 and (ord(p[i]) - ord(p[i - 1]) == 1 or (p[i - 1] == 'z' and p[i] == 'a')):
                curr_len += 1
            else:
                curr_len = 1

            idx = ord(p[i]) - ord('a')
            dp[idx] = max(dp[idx], curr_len)

        return sum(dp)

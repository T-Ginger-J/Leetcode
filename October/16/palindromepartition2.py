class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        dp_pal = [[False] * n for _ in range(n)]
        cuts = [0] * n
        
        for i in range(n):
            min_cut = i
            for j in range(i + 1):
                if s[i] == s[j] and (i - j < 2 or dp_pal[j + 1][i - 1]):
                    dp_pal[j][i] = True
                    min_cut = 0 if j == 0 else min(min_cut, cuts[j - 1] + 1)
            cuts[i] = min_cut
        return cuts[-1]


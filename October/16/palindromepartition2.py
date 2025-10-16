# LeetCode 132: Palindrome Partitioning II
# Explanation:
# 1. Goal: Find the minimum number of cuts needed to partition a string into palindromic substrings.
# 2. Precompute all palindromic substrings using DP (dp_pal[i][j] = True if s[i:j+1] is palindrome).
# 3. Use another DP array `cuts[i]` to store the minimum cuts for substring s[:i+1].
# 4. For each i, check all j ≤ i; if s[j:i+1] is palindrome, update cuts[i] = min(cuts[i], cuts[j-1]+1).
# Time Complexity: O(n²)
# Space Complexity: O(n²)

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


# LeetCode 392: Is Subsequence
# Explanation:
# 1. Use two pointers to traverse s and t
# 2. If all characters of s are found in t in order, return True
# Time Complexity: O(n + m)
# Space Complexity: O(1)

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0  # pointer for s
        for ch in t:
            if i < len(s) and s[i] == ch:
                i += 1
        return i == len(s)


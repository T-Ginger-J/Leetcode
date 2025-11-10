# LeetCode 214: Shortest Palindrome
# Explanation:
# 1. We want the longest prefix of s that is also a palindrome.
# 2. Build new string "s + '#' + reversed(s)".
# 3. Compute KMP prefix table to find longest matching prefix-suffix.
# 4. Add the remaining reversed suffix to the front.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev = s[::-1]
        new_s = s + "#" + rev
        lps = [0] * len(new_s)

        for i in range(1, len(new_s)):
            j = lps[i-1]
            while j > 0 and new_s[i] != new_s[j]:
                j = lps[j-1]
            if new_s[i] == new_s[j]:
                j += 1
            lps[i] = j

        add_len = len(s) - lps[-1]
        return rev[:add_len] + s

    def shortestPalindromeTwoPointer(self, s: str) -> str:
        i = 0
        for j in range(len(s)-1, -1, -1):
            if s[i] == s[j]:
                i += 1
        if i == len(s): 
            return s
        suffix = s[i:]
        return suffix[::-1] + self.shortestPalindrome(s[:i]) + suffix


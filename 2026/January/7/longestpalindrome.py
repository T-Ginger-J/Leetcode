# LeetCode 409: Longest Palindrome
# Explanation:
# 1. Count character frequencies
# 2. Use all even counts, for odd counts use count-1
# 3. Add 1 if any odd exists for the center
# Time Complexity: O(n)
# Space Complexity: O(1)

from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        length = 0
        odd_found = False
        for c in counts.values():
            if c % 2 == 0:
                length += c
            else:
                length += c - 1
                odd_found = True
        return length + 1 if odd_found else length

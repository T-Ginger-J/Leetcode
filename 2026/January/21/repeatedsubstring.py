# LeetCode 459: Repeated Substring Pattern
# Explanation:
# Given a string s, determine if it can be formed by repeating a substring multiple times.
#
# Method 1: KMP / String Manipulation (Optimal)
# - Check if s is in (s+s)[1:-1]. If yes, it has a repeated substring pattern.
# - Intuition: By doubling the string and removing first and last characters,
#   the original string will appear inside if it's composed of a repeated substring.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]

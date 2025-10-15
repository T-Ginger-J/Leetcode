# LeetCode 125: Valid Palindrome
# Explanation:
# 1. Convert string to lowercase and keep only alphanumeric characters.
# 2. Compare filtered string to its reverse.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
        return filtered == filtered[::-1]

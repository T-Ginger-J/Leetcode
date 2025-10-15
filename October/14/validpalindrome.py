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

    def isPalindromePointers(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
# Output: True

print(Solution().isPalindrome("race a car"))
# Output: False

print(Solution().isPalindrome(" "))
# Output: True


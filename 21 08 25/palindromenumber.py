class Solution:
    def isPalindrome(self, x):
        # Negative numbers are not palindromes
        if x < 0:
            return False
        # Convert to string and check reverse
        s = str(x)
        return s == s[::-1]
    
    def isPalindromeStringless(self, x):
        # Negative numbers are not palindromes
        if x < 0:
            return False
        # Numbers ending with 0 (but not 0 itself) are not palindromes
        if x % 10 == 0 and x != 0:
            return False

        rev = 0
        while x > rev:
            rev = rev * 10 + x % 10
            x //= 10   # floor division for integer

        # For even length: x == rev
        # For odd length: x == rev // 10
        return x == rev or x == rev // 10

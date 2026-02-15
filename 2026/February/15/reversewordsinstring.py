# LeetCode 557: Reverse Words in a String III
# Explanation:
# 1. Given a string s containing words separated by spaces, reverse each word individually while keeping word order.
# 2. Approach:
#    - Split the string by spaces.
#    - Reverse each word using slicing or reversed().
#    - Join the words back with spaces.
# 3. Time Complexity: O(n), n = length of string
# 4. Space Complexity: O(n), for storing words and reversed result

class Solution:

    # -------------------------------------------------------
    # Method 1: Split and reverse each word
    # -------------------------------------------------------
    def reverseWords(self, s: str) -> str:
        return ' '.join(word[::-1] for word in s.split(' '))

    # -------------------------------------------------------
    # Method 2: In-place character list manipulation
    # -------------------------------------------------------
    def reverseWordsInPlace(self, s: str) -> str:
        chars = list(s)
        start = 0
        n = len(chars)
        for i in range(n+1):
            if i == n or chars[i] == ' ':
                l, r = start, i-1
                while l < r:
                    chars[l], chars[r] = chars[r], chars[l]
                    l += 1
                    r -= 1
                start = i+1
        return ''.join(chars)


# -------------------------------------------------------
# Examples & Edge Cases
# -------------------------------------------------------

sol = Solution()

# Example 1
s1 = "Let's take LeetCode contest"
print(sol.reverseWords(s1))          # "s'teL ekat edoCteeL tsetnoc"
print(sol.reverseWordsInPlace(s1))   # "s'teL ekat edoCteeL tsetnoc"

# Example 2: Single word
s2 = "Hello"
print(sol.reverseWords(s2))          # "olleH"

# Example 3: Empty string
s3 = ""
print(sol.reverseWords(s3))          # ""

# Example 4: Multiple spaces
s4 = "a b  c"
print(sol.reverseWords(s4))          # "a b  c"

# Example 5: Palindrome words
s5 = "madam noon civic"
print(sol.reverseWords(s5))          # "madam noon civic"

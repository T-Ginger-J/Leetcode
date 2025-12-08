# LeetCode 345: Reverse Vowels of a String
# Explanation:
# 1. Convert string to list (since Python str is immutable).
# 2. Use two pointers to locate vowels and swap.
# 3. Join the list back to a string.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def reverseVowels(self, s):
        vowels = set("aeiouAEIOU")
        s = list(s)
        l, r = 0, len(s) - 1

        while l < r:
            while l < r and s[l] not in vowels:
                l += 1
            while l < r and s[r] not in vowels:
                r -= 1

            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        return "".join(s)

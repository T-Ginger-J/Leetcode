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

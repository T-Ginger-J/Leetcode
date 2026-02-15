class Solution:

    # -------------------------------------------------------
    # Method 1: Split and reverse each word
    # -------------------------------------------------------
    def reverseWords(self, s: str) -> str:
        return ' '.join(word[::-1] for word in s.split(' '))

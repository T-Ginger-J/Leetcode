# LeetCode 58: Length of Last Word
# Explanation:
# 1. strip() removes trailing/leading spaces.
# 2. split() breaks the string into words by spaces.
# 3. words[-1] gives the last word.
# 4. len() returns its length.
# Time Complexity: O(n) where n = length of s

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.strip().split()
        return len(words[-1])
    
    def lengthOfLastWordVerbose(self, s: str) -> int:
        i = len(s) - 1
        length = 0
        while i >= 0 and s[i] == ' ':
            i -= 1
        while i >= 0 and s[i] != ' ':   
            length += 1
            i -= 1
        return length
    
    lengthOfLastWordOneLine = lambda s: len(s.strip().split()[-1])

# Example usage:
# sol = Solution()
# print(sol.lengthOfLastWord("Hello World"))           # 5
# print(sol.lengthOfLastWord("   fly me   to   the moon  ")) # 4
# print(sol.lengthOfLastWord("a"))                     # 1

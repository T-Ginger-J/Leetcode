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
    

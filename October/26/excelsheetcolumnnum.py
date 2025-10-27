# LeetCode 171: Excel Sheet Column Number
# Explanation:
# 1. Excel column titles are base-26 (A=1, B=2, ..., Z=26).
# 2. Convert the string to a number using positional base-26 math.
# 3. For each character, multiply current total by 26 and add the character’s value.
# Time Complexity: O(n) where n = len(columnTitle)
# Space Complexity: O(1)

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        for c in columnTitle:
            result = result * 26 + (ord(c) - ord('A') + 1)
        return result

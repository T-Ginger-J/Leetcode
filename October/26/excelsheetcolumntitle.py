# LeetCode 168: Excel Sheet Column Title
# Explanation:
# 1. Convert a number (1-based) to an Excel column title (A-Z, AA, AB...).
# 2. Similar to converting to base-26 but with offset (since Excel starts from 1, not 0).
# 3. Subtract 1 before modulus and division to align with alphabet indices (0–25).
# 4. Build string in reverse order and reverse it at the end.
# Time Complexity: O(log₍₂₆₎n)
# Space Complexity: O(log₍₂₆₎n)

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber -= 1
            result = chr(columnNumber % 26 + ord('A')) + result
            columnNumber //= 26
        return result

# LeetCode 500: Keyboard Row
# Explanation:
# Given an array of strings words, return the words that can be typed using
# letters of only one row on the American keyboard.
#
# Method 1: Set Membership (Optimal)
# - Define sets for each keyboard row.
# - A word is valid if all its characters belong to the same row.
#
# Time Complexity: O(total_characters)
# Space Complexity: O(1)

from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        res = []
        for word in words:
            w = set(word.lower())
            if w <= row1 or w <= row2 or w <= row3:
                res.append(word)
        return res


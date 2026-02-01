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


# Alternate Python Solution: Character-to-Row Mapping
# - Map each character to its keyboard row index.
# - Check that all characters in a word map to the same row.

class SolutionMap:
    def findWords(self, words: List[str]) -> List[str]:
        row_map = {}
        for c in "qwertyuiop":
            row_map[c] = 1
        for c in "asdfghjkl":
            row_map[c] = 2
        for c in "zxcvbnm":
            row_map[c] = 3

        res = []
        for word in words:
            rows = {row_map[c] for c in word.lower()}
            if len(rows) == 1:
                res.append(word)
        return res

# LeetCode 524: Longest Word in Dictionary through Deleting
# Explanation:
# 1. We are given a string s and a list of dictionary words.
# 2. We need the longest word that can be formed by deleting characters from s.
# 3. If multiple answers exist, return the smallest lexicographical one.
# 4. A word is valid if it is a subsequence of s.

# Methods Used:
# - Two-Pointer Subsequence Check
# - Sorting + Greedy Selection
# - Preprocessing with Next-Occurrence Table

# Time Complexity:
# - Two-Pointer: O(n * L)
#   n = number of words, L = length of s
# - Preprocessing: O(26 * L + n * m)

# Space Complexity:
# - O(1) for two-pointer
# - O(26 * L) for preprocessing


from typing import List


class Solution:

    # -------------------------------------------------------
    # Method 1: Sorting + Two-Pointer (Optimal for Constraints)
    # -------------------------------------------------------
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:

        # Sort by length desc, lex asc
        dictionary.sort(key=lambda x: (-len(x), x))

        def isSubseq(word, s):
            i = 0
            for ch in s:
                if i < len(word) and word[i] == ch:
                    i += 1
            return i == len(word)

        for word in dictionary:
            if isSubseq(word, s):
                return word

        return ""

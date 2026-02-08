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

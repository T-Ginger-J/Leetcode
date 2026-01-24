# LeetCode 472: Concatenated Words
# Explanation:
# Given a list of words, return all words that are formed by concatenating
# at least two shorter words from the same list.
#
# Method 1: DFS + Memoization (Optimal)
# - Insert all words into a set for O(1) lookup.
# - For each word, try to split it into prefix + suffix.
# - If prefix is a word and suffix is either a word or can be recursively formed,
#   then the word is a concatenated word.
# - Use memoization to avoid recomputation.
#
# Time Complexity: O(N * L^2)
#   where N = number of words, L = max word length
# Space Complexity: O(N * L)

from typing import List
from functools import lru_cache

class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)

        @lru_cache(None)
        def can_form(word: str) -> bool:
            for i in range(1, len(word)):
                prefix = word[:i]
                suffix = word[i:]
                if prefix in word_set and (suffix in word_set or can_form(suffix)):
                    return True
            return False

        result = []
        for w in words:
            if w and can_form(w):
                result.append(w)
        return result


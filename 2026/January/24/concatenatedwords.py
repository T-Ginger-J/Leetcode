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


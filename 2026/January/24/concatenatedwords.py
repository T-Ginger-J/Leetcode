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


# Alternate Python Solution: DP Word Break Style
# - For each word, use DP where dp[i] means word[:i] can be formed.
# - Ensure at least two words are used by disallowing the whole word as a single piece.

class SolutionDP:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        word_set = set(words)
        res = []

        for word in words:
            if not word:
                continue
            n = len(word)
            dp = [False] * (n + 1)
            dp[0] = True

            for i in range(1, n + 1):
                for j in range(i):
                    if not dp[j]:
                        continue
                    if word[j:i] in word_set and not (j == 0 and i == n):
                        dp[i] = True
                        break

            if dp[n]:
                res.append(word)

        return res


# Additional Examples (Edge Cases and Non-LeetCode Examples)

sol = Solution()

# Example 1: Simple concatenation
print(sol.findAllConcatenatedWordsInADict(
    ["cat", "cats", "dog", "catsdog"]
))
# Expected output: ["catsdog"]

# Example 2: Multiple levels of concatenation
print(sol.findAllConcatenatedWordsInADict(
    ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa"]
))
# Expected output: ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa"]

# Example 3: No concatenated words
print(sol.findAllConcatenatedWordsInADict(
    ["apple", "banana", "orange"]
))
# Expected output: []

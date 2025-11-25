# LeetCode 290: Word Pattern
# Explanation:
# 1. We need to check if a pattern (string of letters) matches a string of words.
# 2. Use two dictionaries (or one dictionary + one set) to ensure a bijection:
#    - pattern letter -> word
#    - word -> pattern letter
# 3. Iterate through pattern and words simultaneously:
#    - If mapping exists, check consistency.
#    - If mapping does not exist, create it.
# 4. If any inconsistency is found, return False.
# Time Complexity: O(n) where n is number of words
# Space Complexity: O(n), for storing mappings

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        p2w, w2p = {}, {}
        for p, w in zip(pattern, words):
            if p in p2w and p2w[p] != w:
                return False
            if w in w2p and w2p[w] != p:
                return False
            p2w[p] = w
            w2p[w] = p
        return True

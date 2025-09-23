# LeetCode 68: Text Justification
# Explanation:
# 1. Greedily pick words that fit within maxWidth.
# 2. If it's the last line or only one word, left-justify.
# 3. Otherwise, distribute spaces evenly across gaps.
# Time Complexity: O(n * L) where n = number of words, L = maxWidth
# Space Complexity: O(1)

class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]

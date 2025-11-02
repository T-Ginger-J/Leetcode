# LeetCode 192: Word Frequency
# Explanation:
# 1. Read the file words.txt, split into words by whitespace.
# 2. Count frequencies using a dictionary.
# 3. Sort by frequency descending.
# Time Complexity: O(n log n) where n = number of words (for sorting)
# Space Complexity: O(n)

from collections import Counter

class Solution:
    def wordFrequency(self, words: str):
        # words: string contents of words.txt
        freq = {}
        for w in words.split():
            freq[w] = freq.get(w, 0) + 1
        # sort by frequency descending
        sorted_items = sorted(freq.items(), key=lambda x: -x[1])
        return [(w, c) for w, c in sorted_items]
    def wordFrequencyOneLine(self, words: str): return __import__('collections').Counter(words.split()).most_common()


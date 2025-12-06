# LeetCode 336: Palindrome Pairs
# Explanation:
# 1. Use a hash map to store reversed words -> index.
# 2. For each word, try every split into prefix + suffix.
# 3. Check:
#    - If prefix is palindrome, and reversed(suffix) exists → add (reversed_index, current_index)
#    - If suffix is palindrome, and reversed(prefix) exists → add (current_index, reversed_index)
# 4. Avoid duplicates by skipping empty suffix for suffix-palindrome case.
# Time Complexity: O(n * k^2), n = number of words, k = max word length
# Space Complexity: O(n * k)

class Solution:
    def palindromePairs(self, words):
        rev_map = {w[::-1]: i for i, w in enumerate(words)}
        res = []

        def is_pal(s):
            return s == s[::-1]

        for i, word in enumerate(words):
            for cut in range(len(word) + 1):
                prefix, suffix = word[:cut], word[cut:]
                
                if is_pal(prefix) and suffix in rev_map and rev_map[suffix] != i:
                    res.append([rev_map[suffix], i])
                if cut != len(word) and is_pal(suffix) and prefix in rev_map and rev_map[prefix] != i:
                    res.append([i, rev_map[prefix]])
        return res


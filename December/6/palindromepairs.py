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


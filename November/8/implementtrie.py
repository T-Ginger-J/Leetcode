# LeetCode 208: Implement Trie (Prefix Tree)
# Explanation:
# 1. Use a nested dictionary to represent Trie nodes.
# 2. '#' marks the end of a word.
# 3. Insert: traverse and create missing nodes.
# 4. Search: traverse; ensure '#' exists at the end.
# 5. startsWith: check prefix existence only.
# Time Complexity: O(L) per operation, where L = length of word/prefix
# Space Complexity: O(N * L) for all words stored

class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        node = self.trie
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node['#'] = True  # word end marker

    def search(self, word: str) -> bool:
        node = self.trie
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return '#' in node

    def startsWith(self, prefix: str) -> bool:
        node = self.trie
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True

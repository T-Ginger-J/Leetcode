# LeetCode 211: Design Add and Search Words Data Structure
# Explanation:
# 1. Use Trie nodes (dicts) where each node maps char -> next node.
# 2. For addWord: traverse and create child nodes.
# 3. For search: DFS all possible paths when '.' is found.
# Time Complexity: O(M) for addWord, O(N * 26^d) worst for search where d = number of dots.
# Space Complexity: O(T) total characters stored.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.end = True

    def search(self, word: str) -> bool:
        def dfs(node, i):
            if i == len(word):
                return node.end
            if word[i] == '.':
                return any(dfs(child, i+1) for child in node.children.values())
            if word[i] not in node.children:
                return False
            return dfs(node.children[word[i]], i+1)
        return dfs(self.root, 0)

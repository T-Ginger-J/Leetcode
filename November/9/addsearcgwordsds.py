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

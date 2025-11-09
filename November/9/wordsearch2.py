# LeetCode 212: Word Search II
# Explanation:
# 1. Build a Trie to efficiently check prefixes and complete words.
# 2. For each board cell, perform DFS with backtracking.
# 3. Prune search when prefix not in Trie; mark visited cells temporarily.
# Time Complexity: O(M * N * 4^L), where L = max word length.
# Space Complexity: O(T + M*N), where T = total chars in words.

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        root = TrieNode()
        for w in words:
            node = root
            for c in w:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
            node.word = w
        
        res = []
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c, node):
            char = board[r][c]
            if char not in node.children:
                return
            nxt = node.children[char]
            if nxt.word:
                res.append(nxt.word)
                nxt.word = None  # avoid duplicates

            board[r][c] = '#'
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] != '#':
                    dfs(nr, nc, nxt)
            board[r][c] = char

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)
        
        return res

sol = Solution()
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
print(sol.findWords(board, ["oath","pea","eat","rain"]))  # ["eat","oath"]

board = [["a","b"],["c","d"]]
print(sol.findWords(board, ["abcb"]))  # []

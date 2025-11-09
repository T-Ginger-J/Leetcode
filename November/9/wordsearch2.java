// LeetCode 212: Word Search II
// Explanation:
// 1. Build Trie of words for prefix-based pruning.
// 2. Perform DFS from each board cell to find matches.
// 3. Use backtracking and remove found words to avoid duplicates.
// Time Complexity: O(M * N * 4^L)
// Space Complexity: O(T + M*N)

import java.util.*;

class Solution {
    class TrieNode {
        Map<Character, TrieNode> children = new HashMap<>();
        String word = null;
    }

    public List<String> findWords(char[][] board, String[] words) {
        TrieNode root = new TrieNode();
        for (String w : words) {
            TrieNode node = root;
            for (char c : w.toCharArray())
                node = node.children.computeIfAbsent(c, k -> new TrieNode());
            node.word = w;
        }

        List<String> res = new ArrayList<>();
        int rows = board.length, cols = board[0].length;
        for (int r = 0; r < rows; r++)
            for (int c = 0; c < cols; c++)
                dfs(board, r, c, root, res);
        return res;
    }

    private void dfs(char[][] board, int r, int c, TrieNode node, List<String> res) {
        char ch = board[r][c];
        if (!node.children.containsKey(ch)) return;
        TrieNode next = node.children.get(ch);
        if (next.word != null) {
            res.add(next.word);
            next.word = null;
        }

        board[r][c] = '#';
        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};
        for (int[] d : dirs) {
            int nr = r + d[0], nc = c + d[1];
            if (nr >= 0 && nr < board.length && nc >= 0 && nc < board[0].length && board[nr][nc] != '#')
                dfs(board, nr, nc, next, res);
        }
        board[r][c] = ch;
        if (next.children.isEmpty()) node.children.remove(ch);
    }
}


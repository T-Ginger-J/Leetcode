# LeetCode 126: Word Ladder II
# Explanation:
# 1. Use BFS to build a graph of shortest transformation sequences.
# 2. Each word differs by one letter.
# 3. Use backtracking to reconstruct all shortest paths.
# Time Complexity: O(n * L^2) where n = number of words, L = word length
# Space Complexity: O(n * L)

from collections import defaultdict, deque

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        graph = defaultdict(list)
        layer = {beginWord: [[beginWord]]}

        while layer:
            new_layer = defaultdict(list)
            for word in layer:
                if word == endWord:
                    return layer[word]
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i] + c + word[i+1:]
                        if newWord in wordSet:
                            new_layer[newWord] += [path + [newWord] for path in layer[word]]
            wordSet -= set(new_layer.keys())
            layer = new_layer

        return []

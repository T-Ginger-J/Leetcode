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
    
    def findLaddersSpaceoptimized(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []
        
        front, back = {beginWord}, {endWord}
        parents = defaultdict(set)
        reversed = False
        found = False

        while front and not found:
            wordSet -= front
            next_front = set()
            for word in front:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i] + c + word[i+1:]
                        if newWord not in wordSet:
                            continue
                        if newWord in back:
                            found = True
                        next_front.add(newWord)
                        if reversed:
                            parents[newWord].add(word)
                        else:
                            parents[word].add(newWord)
            front = next_front
            if len(front) > len(back):
                front, back, reversed = back, front, not reversed
        
        def buildPaths(word):
            if word == endWord:
                return [[word]]
            return [[word] + rest for nxt in parents[word] for rest in buildPaths(nxt)]

        return buildPaths(beginWord)


print(Solution().findLadders("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
# Output: [["hit","hot","dot","dog","cog"], ["hit","hot","lot","log","cog"]]

print(Solution().findLadders("hit", "cog", ["hot","dot","dog","lot","log"]))
# Output: []

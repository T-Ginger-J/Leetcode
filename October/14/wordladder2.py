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

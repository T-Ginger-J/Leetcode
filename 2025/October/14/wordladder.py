# LeetCode 127: Word Ladder
# Explanation:
# 1. Use BFS to find the shortest transformation from beginWord to endWord.
# 2. Each word can change one letter at a time and must exist in wordList.
# 3. Each level of BFS represents a transformation step.
# Time Complexity: O(n * L^2) where n = number of words, L = length of each word
# Space Complexity: O(n * L)

from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        queue = deque([(beginWord, 1)])
        while queue:
            word, length = queue.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    nextWord = word[:i] + c + word[i+1:]
                    if nextWord in wordSet:
                        wordSet.remove(nextWord)
                        queue.append((nextWord, length + 1))
        return 0

    def ladderLengthOptimized(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        front, back = {beginWord}, {endWord}
        level = 1
        while front and back:
            if len(front) > len(back):
                front, back = back, front
            next_front = set()
            for word in front:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        newWord = word[:i] + c + word[i+1:]
                        if newWord in back:
                            return level + 1
                        if newWord in wordSet:
                            wordSet.remove(newWord)
                            next_front.add(newWord)
            front = next_front
            level += 1
        return 0

print(Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
# Output: 5  (hit -> hot -> dot -> dog -> cog)

print(Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))
# Output: 0  (no valid transformation)

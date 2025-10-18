# LeetCode 140: Word Break II
# Explanation:
# 1. Goal: Return all possible sentences that can be built by segmenting s into words from wordDict.
# 2. Use DFS + memoization:
#    - At each index, try every word that matches a prefix.
#    - Recursively build sentences for remaining substring.
#    - Cache results to avoid recomputation.
# 3. Combine valid segments with spaces.
# Time Complexity: O(n^3) (due to substring + recursion)
# Space Complexity: O(n^2) (for recursion and memoization)

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        wordSet = set(wordDict)
        memo = {}

        def dfs(start):
            if start == len(s):
                return [""]
            if start in memo:
                return memo[start]

            res = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in wordSet:
                    for sub in dfs(end):
                        res.append((word + " " + sub).strip())
            memo[start] = res
            return res

        return dfs(0)

print(Solution().wordBreak("catsanddog", ["cat","cats","and","sand","dog"]))
# Output: ["cats and dog", "cat sand dog"]

print(Solution().wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]))
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]

print(Solution().wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
# Output: []

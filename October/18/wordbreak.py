# LeetCode 139: Word Break
# Explanation:
# 1. Use dynamic programming to check if a string can be segmented into dictionary words.
# 2. dp[i] = True if s[:i] can be segmented using words in wordDict.
# 3. For each index i, check every word in wordDict — if word ends at i and dp[start] is True, mark dp[i] = True.
# 4. Return dp[n] at the end.
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(1, len(s) + 1):
            for word in wordSet:
                if i >= len(word) and dp[i - len(word)] and s[i - len(word):i] == word:
                    dp[i] = True
                    break
        return dp[-1]

print(Solution().wordBreak("leetcode", ["leet", "code"]))
# Output: True

print(Solution().wordBreak("applepenapple", ["apple", "pen"]))
# Output: True

print(Solution().wordBreak("catsandog", ["cats","dog","sand","and","cat"]))
# Output: False

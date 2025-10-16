# LeetCode 131: Palindrome Partitioning
# Explanation:
# 1. Goal: Partition string s so every substring is a palindrome.
# 2. Use DFS with backtracking to explore all partitions.
# 3. At each position, expand substring and recurse if it’s a palindrome.
# 4. Store and return all valid partitions.
# Time Complexity: O(n * 2^n), where n = len(s)
# Space Complexity: O(n)

class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []

        def is_palindrome(sub):
            return sub == sub[::-1]

        def dfs(start, path):
            if start == len(s):
                res.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    dfs(end, path + [s[start:end]])

        dfs(0, [])
        return res

    def partitionBacktrack(self, s: str) -> list[list[str]]:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                dp[i][j] = s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1])

        res = []

        def dfs(start, path):
            if start == n:
                res.append(path[:])
                return
            for end in range(start, n):
                if dp[start][end]:
                    dfs(end + 1, path + [s[start:end + 1]])

        dfs(0, [])
        return res
    

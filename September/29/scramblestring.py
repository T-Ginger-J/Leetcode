# LeetCode 87: Scramble String
# Explanation:
# 1. Use recursion with memoization to check if s2 is scrambled version of s1.
# 2. Base cases: equal strings -> True, different sorted chars -> False.
# 3. Try all possible partitions; check if swapped or not swapped parts are scrambled.
# Time Complexity: O(n^4) worst case due to recursion + substring splits.
# Space Complexity: O(n^3) for memoization.

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache(None)
        def dfs(a, b):
            if a == b:
                return True
            if sorted(a) != sorted(b):
                return False
            n = len(a)
            for i in range(1, n):
                if (dfs(a[:i], b[:i]) and dfs(a[i:], b[i:])) or \
                   (dfs(a[:i], b[-i:]) and dfs(a[i:], b[:-i])):
                    return True
            return False
        return dfs(s1, s2)

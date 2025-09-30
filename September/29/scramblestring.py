# LeetCode 87: Scramble String
# Explanation:
# 1. Use recursion with memoization to check if s2 is scrambled version of s1.
# 2. Base cases: equal strings -> True, different sorted chars -> False.
# 3. Try all possible partitions; check if swapped or not swapped parts are scrambled.
# Time Complexity: O(n^4) worst case due to recursion + substring splits.
# Space Complexity: O(n^3) for memoization.

from functools import lru_cache

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

    def __init__(self):
        # memo dictionary to store previously computed results
        self.memo = {}

    def isScrambleMemoization(self, s1: str, s2: str) -> bool:
        n = len(s1)

        # base case: identical strings are trivially scramble
        if s1 == s2:
            return True

        # check memoized result
        key = s1 + "|" + s2
        if key in self.memo:
            return self.memo[key]

        # frequency arrays for pruning
        count_s1, count_s2, count_s2_rev = [0] * 26, [0] * 26, [0] * 26

        for i in range(1, n):
            j = n - i  # suffix index for swapped case

            # update frequency counts
            count_s1[ord(s1[i - 1]) - ord('a')] += 1
            count_s2[ord(s2[i - 1]) - ord('a')] += 1
            count_s2_rev[ord(s2[j]) - ord('a')] += 1

            # case 1: no swap
            if count_s1 == count_s2:
                if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                    self.memo[key] = True
                    return True

            # case 2: swapped
            if count_s1 == count_s2_rev:
                if self.isScramble(s1[:i], s2[j:]) and self.isScramble(s1[i:], s2[:j]):
                    self.memo[key] = True
                    return True

        self.memo[key] = False
        return False  

# LeetCode 488: Zuma Game
# Explanation:
# Given a string board of colored balls and a string hand, determine the
# minimum number of balls you need to insert from hand to clear the board.
# If impossible, return -1.
#
# Method 1: DFS + Backtracking with Pruning
# - Try inserting each ball in hand at every possible position where it
#   can help form a group of 3 or more.
# - Recursively clear the board after each insertion.
# - Use memoization to avoid recomputation.
#
# Time Complexity: Exponential in worst case (pruned by memoization)
# Space Complexity: O(n * len(hand))

from functools import lru_cache

class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        from collections import Counter

        @lru_cache(None)
        def dfs(s, h):
            if not s:
                return 0
            if not h:
                return float('inf')
            res = float('inf')
            n = len(s)
            i = 0
            while i < n:
                j = i
                while j < n and s[j] == s[i]:
                    j += 1
                need = 3 - (j - i)
                if h.count(s[i]) >= need:
                    new_hand = h.replace(s[i], '', need)
                    new_s = s[:i] + s[j:]
                    # recursively clear consecutive balls
                    new_s = clear(new_s)
                    res = min(res, need + dfs(new_s, new_hand))
                i = j
            return res

        def clear(s):
            i = 0
            n = len(s)
            while i < n:
                j = i
                while j < n and s[j] == s[i]:
                    j += 1
                if j - i >= 3:
                    s = s[:i] + s[j:]
                    n = len(s)
                    i = 0
                else:
                    i += 1
            return s

        ans = dfs(board, hand)
        return ans if ans != float('inf') else -1


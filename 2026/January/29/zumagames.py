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


# Alternate Python Solution: DFS with Counter from collections
# - Precompute hand counts
# - Simplify insertion simulation

from collections import Counter

class SolutionCounter:
    def findMinStep(self, board: str, hand: str) -> int:
        hand_count = Counter(hand)

        @lru_cache(None)
        def dfs(b):
            if not b:
                return 0
            res = float('inf')
            i = 0
            while i < len(b):
                j = i
                while j < len(b) and b[j] == b[i]:
                    j += 1
                need = max(0, 3 - (j - i))
                if hand_count[b[i]] >= need:
                    hand_count[b[i]] -= need
                    res = min(res, need + dfs(clear(b[:i] + b[j:])))
                    hand_count[b[i]] += need
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

        ans = dfs(board)
        return ans if ans != float('inf') else -1


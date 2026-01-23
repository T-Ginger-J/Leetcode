# LeetCode 464: Can I Win
# Explanation:
# Two players take turns choosing numbers from 1 to maxChoosableInteger (each used once).
# The running total increases by the chosen number.
# The player who reaches or exceeds desiredTotal wins.
#
# Method 1: DFS + Bitmask DP (Optimal)
# - Use a bitmask to represent which numbers are already used.
# - Memoize game states: can the current player force a win from this state?
# - Try all unused numbers; if choosing one forces the opponent into a losing state,
#   current player can win.
#
# Key Pruning:
# - If sum(1..maxChoosableInteger) < desiredTotal → impossible to win.
#
# Time Complexity: O(2^n * n)
# Space Complexity: O(2^n)

from functools import lru_cache

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True
        total_sum = maxChoosableInteger * (maxChoosableInteger + 1) // 2
        if total_sum < desiredTotal:
            return False

        @lru_cache(None)
        def dfs(used_mask: int, remaining: int) -> bool:
            for i in range(1, maxChoosableInteger + 1):
                bit = 1 << (i - 1)
                if used_mask & bit == 0:
                    if i >= remaining:
                        return True
                    if not dfs(used_mask | bit, remaining - i):
                        return True
            return False

        return dfs(0, desiredTotal)


# Additional Examples (Edge Cases and Non-LeetCode Examples)

sol = Solution()

# Example 1: Immediate win possible
print(sol.canIWin(10, 1))
# Expected output: True

# Example 2: Impossible to reach desired total
print(sol.canIWin(5, 50))
# Expected output: False

# Example 3: Tight strategic game
print(sol.canIWin(6, 10))
# Expected output: True

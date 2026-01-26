# LeetCode 473: Matchsticks to Square
# Explanation:
# Given an array matchsticks, determine if you can form a square
# using all matchsticks exactly once.
#
# Conditions:
# - All 4 sides must have equal length.
# - Total length must be divisible by 4.
#
# Method 1: Backtracking with Pruning (Optimal)
# - Compute target side length = sum(matchsticks) / 4.
# - Sort matchsticks in descending order (pruning optimization).
# - Try to assign each matchstick to one of the 4 sides.
# - If any side exceeds target, backtrack.
#
# Time Complexity: O(4^n) in worst case
# Space Complexity: O(n) recursion stack

from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks or sum(matchsticks) % 4 != 0:
            return False

        target = sum(matchsticks) // 4
        matchsticks.sort(reverse=True)
        sides = [0] * 4

        def backtrack(index):
            if index == len(matchsticks):
                return all(side == target for side in sides)

            for i in range(4):
                if sides[i] + matchsticks[index] > target:
                    continue
                sides[i] += matchsticks[index]
                if backtrack(index + 1):
                    return True
                sides[i] -= matchsticks[index]
                if sides[i] == 0:
                    break
            return False

        return backtrack(0)


# Alternate Python Solution: Bitmask DP
# - dp[mask] = current side length modulo target
# - If dp[mask] == 0 and mask != 0, one side is completed.
#
# Time Complexity: O(n * 2^n)
# Space Complexity: O(2^n)

class SolutionDP:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if total % 4 != 0:
            return False

        target = total // 4
        n = len(matchsticks)
        dp = [-1] * (1 << n)
        dp[0] = 0

        for mask in range(1 << n):
            if dp[mask] == -1:
                continue
            for i in range(n):
                if not (mask & (1 << i)):
                    if dp[mask] + matchsticks[i] <= target:
                        nxt = mask | (1 << i)
                        dp[nxt] = (dp[mask] + matchsticks[i]) % target
        return dp[(1 << n) - 1] == 0

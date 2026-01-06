# LeetCode 403: Frog Jump
# Explanation:
# 1. Map each stone position to the set of jump sizes that can reach it
# 2. Iterate stones, update reachable jumps for next stones
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

class Solution:
    def canCross(self, stones: list[int]) -> bool:
        stone_set = set(stones)
        dp = {stone: set() for stone in stones}
        dp[0].add(0)
        for stone in stones:
            for k in dp[stone]:
                for step in [k-1, k, k+1]:
                    if step > 0 and (stone + step) in stone_set:
                        dp[stone + step].add(step)
        return len(dp[stones[-1]]) > 0

# LeetCode 458: Poor Pigs
# Explanation:
# Given buckets with one poisonous bucket, and pigs that die in `minutesToDie` minutes,
# find the minimum number of pigs needed to determine the poisonous bucket within
# `minutesToTest` minutes.
#
# Key Insight:
# - Each pig can test multiple times (rounds = minutesToTest // minutesToDie + 1)
#   because each pig can survive multiple tests if we schedule them properly.
# - Number of states per pig = rounds
# - Total combinations = (rounds) ** pigs
# - We need combinations >= buckets → find minimum pigs

import math

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        rounds = minutesToTest // minutesToDie + 1
        pigs = 0
        while rounds ** pigs < buckets:
            pigs += 1
        return pigs


# Additional Examples (Edge Cases and Non-LeetCode Examples)

sol = Solution()

# Example 1: Simple case
print(sol.poorPigs(1000, 15, 60))
# Expected output: 5
# Explanation: 4 rounds per pig (60/15+1), 4^5=1024 >= 1000

# Example 2: Minimum buckets
print(sol.poorPigs(1, 15, 60))
# Expected output: 0
# Explanation: Only one bucket, no pigs needed

# Example 3: Just enough rounds
print(sol.poorPigs(4, 15, 15))
# Expected output: 2
# Explanation: Only 1 round per pig (15/15+1=2), 2^2=4

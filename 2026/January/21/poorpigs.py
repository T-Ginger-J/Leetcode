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

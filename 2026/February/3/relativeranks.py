# LeetCode 506: Relative Ranks
# Explanation:
# Given an array of unique scores, assign ranks:
# - Highest score -> "Gold Medal"
# - 2nd highest -> "Silver Medal"
# - 3rd highest -> "Bronze Medal"
# - Others -> their rank number as a string
#
# Method 1: Sorting with Index Mapping (Optimal)
# - Sort indices by score descending.
# - Assign medals/ranks based on sorted order.
#
# Time Complexity: O(n log n)
# Space Complexity: O(n)

from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        res = [""] * n
        order = sorted(range(n), key=lambda i: -score[i])

        for rank, idx in enumerate(order, start=1):
            if rank == 1:
                res[idx] = "Gold Medal"
            elif rank == 2:
                res[idx] = "Silver Medal"
            elif rank == 3:
                res[idx] = "Bronze Medal"
            else:
                res[idx] = str(rank)
        return res

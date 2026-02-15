# LeetCode 550: Game Play Analysis I
# Explanation:
# 1. Given an array of scores for n players, we want to find the number of players
#    who have the highest score at the end of the game (after adding their scores).
# 2. Each score[i] represents the points gained by player i.
# 3. We can calculate the maximum score and count how many players reach it.

# Methods Used:
# - Simple max calculation
# - Count occurrences

# Time Complexity:
# - O(n)

# Space Complexity:
# - O(1)


from typing import List


class Solution:

    # -------------------------------------------------------
    # Method 1: Max + Count
    # -------------------------------------------------------
    def game(self, scores: List[int]) -> int:
        if not scores:
            return 0
        max_score = max(scores)
        return scores.count(max_score)


# -------------------------------------------------------
# Examples (Including Edge Cases)
# -------------------------------------------------------

# Example 1
scores1 = [1,3,2,3]
print(Solution().game(scores1))  # 2 (players with score 3)

# Example 2
scores2 = [5,5,5,5]
print(Solution().game(scores2))  # 4 (all players tied)

# Example 3 (Single player)
scores3 = [10]
print(Solution().game(scores3))  # 1

# Example 4 (Empty list)
scores4 = []
print(Solution().game(scores4))  # 0

# Example 5 (Negative scores)
scores5 = [-1, -2, -1, -3]
print(Solution().game(scores5))  # 2 (-1 is highest)

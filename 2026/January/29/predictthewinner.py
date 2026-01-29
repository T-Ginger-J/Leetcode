# LeetCode 486: Predict the Winner
# Explanation:
# Two players take turns picking numbers from either end of an array.
# Determine if player 1 can win assuming both play optimally.
#
# Method 1: Minimax with Memoization (Optimal)
# - Let dp(i, j) = max score difference the current player can achieve
#   from subarray nums[i..j].
# - Choices:
#     pick left: nums[i] - dp(i+1, j)
#     pick right: nums[j] - dp(i, j-1)
# - Player 1 wins if dp(0, n-1) >= 0
#
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

from typing import List
from functools import lru_cache

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        @lru_cache(None)
        def dp(i, j):
            if i == j:
                return nums[i]
            pick_i = nums[i] - dp(i + 1, j)
            pick_j = nums[j] - dp(i, j - 1)
            return max(pick_i, pick_j)

        return dp(0, n - 1) >= 0


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


# Alternate Python Solution: Bottom-Up DP
# - Use 2D DP table where dp[i][j] = max score difference for nums[i..j]
# - Fill table for increasing length of subarrays

class SolutionDP:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i] = nums[i]

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                dp[i][j] = max(nums[i] - dp[i+1][j], nums[j] - dp[i][j-1])

        return dp[0][n-1] >= 0


# Additional Examples (Edge Cases and Non-LeetCode Examples)

sol = Solution()

# Example 1: Two elements, player1 wins
print(sol.PredictTheWinner([1,5]))
# Expected output: False

# Example 2: Equal numbers
print(sol.PredictTheWinner([1,5,2]))
# Expected output: False

# Example 3: Player1 can win
print(sol.PredictTheWinner([1,5,233,7]))
# Expected output: True

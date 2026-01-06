# LeetCode 221: Maximal Square
# Explanation:
# 1. Use DP table where dp[i][j] = side length of largest square ending at (i, j).
# 2. Recurrence: if matrix[i][j] == '1' => dp[i][j] = min(top, left, top-left) + 1.
# 3. Keep track of the max side seen so far.
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

class Solution:
    def maximalSquare(self, matrix: list[list[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        max_side = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if matrix[i - 1][j - 1] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    max_side = max(max_side, dp[i][j])
        return max_side * max_side

sol = Solution()
print(sol.maximalSquare([
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]))  # 4

print(sol.maximalSquare([["0","1"],["1","0"]]))  # 1
print(sol.maximalSquare([["0"]]))                # 0

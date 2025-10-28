# LeetCode 174: Dungeon Game
# Explanation:
# 1. Work backwards from the bottom-right to determine the minimum health needed at each cell.
# 2. dp[i][j] = max(1, min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j])
#    - dp[i][j] is the min HP needed to survive from that cell to the end.
# 3. Start from bottom-right (princess cell) and move up-left.
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

class Solution:
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        dp[m][n - 1] = dp[m - 1][n] = 1

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                need = min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j]
                dp[i][j] = 1 if need <= 0 else need
        return dp[0][0]

    def calculateMinimumHPSpaceOptimized(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        dp = [float('inf')] * (n + 1)
        dp[n - 1] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                dp[j] = max(1, min(dp[j], dp[j + 1]) - dungeon[i][j])
        return dp[0]


# LeetCode 419: Battleships in a Board
# Explanation:
# 1. Scan each cell
# 2. Count 'X' only if top-left of a battleship
# Time Complexity: O(m*n)
# Space Complexity: O(1)

class Solution:
    def countBattleships(self, board: list[list[str]]) -> int:
        if not board or not board[0]:
            return 0
        m, n = len(board), len(board[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    if i > 0 and board[i-1][j] == 'X':
                        continue
                    if j > 0 and board[i][j-1] == 'X':
                        continue
                    count += 1
        return count

board = [
    ["X",".",".","X"],
    [".",".",".","X"],
    [".",".",".","X"]
]
print(Solution().countBattleships(board))  # Output: 2

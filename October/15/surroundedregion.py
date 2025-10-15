# LeetCode 130: Surrounded Regions
# Explanation:
# 1. Goal: Capture all 'O' regions completely surrounded by 'X'.
# 2. Mark all 'O's connected to the border (not surrounded).
# 3. Convert unmarked 'O's to 'X' and restore marked ones.
# Steps:
#   - DFS/BFS from all border 'O's to mark them (safe regions).
#   - Flip remaining 'O's to 'X', and marked cells back to 'O'.
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        if not board or not board[0]:
            return
        
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
                return
            board[r][c] = 'E'  # Mark as escaped
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        # Mark all border-connected 'O's
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)
        
        # Convert surrounded 'O' -> 'X', escaped 'E' -> 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'E':
                    board[r][c] = 'O'

# LeetCode 289: Game of Life
# Explanation:
# 1. Each cell has two possible states: live (1) or dead (0).
# 2. We need to compute the next state using the current state of all cells simultaneously.
# 3. Use in-place encoding to avoid extra space:
#    - 0 -> 0 : dead to dead
#    - 1 -> 1 : live to live
#    - 2 -> 1 : live to dead
#    - 3 -> 0 : dead to live
# 4. Count live neighbors using current state & encoded values.
# Time Complexity: O(m*n), visit each cell and check 8 neighbors
# Space Complexity: O(1), in-place modification

class Solution:
    def gameOfLife(self, board):
        m, n = len(board), len(board[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        
        for i in range(m):
            for j in range(n):
                live_neighbors = 0
                for dx, dy in dirs:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and board[x][y] in [1,2]:
                        live_neighbors += 1
                # Rule 1 or 3: live -> dead
                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = 2
                # Rule 4: dead -> live
                if board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 3
        
        # Finalize board
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2: board[i][j] = 0
                if board[i][j] == 3: board[i][j] = 1
        return board


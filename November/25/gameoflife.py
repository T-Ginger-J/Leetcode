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


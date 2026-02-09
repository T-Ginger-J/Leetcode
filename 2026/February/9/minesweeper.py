from typing import List


class Solution:

    # -------------------------------------------------------
    # Method 1: DFS
    # -------------------------------------------------------
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        if not board:
            return board

        m, n = len(board), len(board[0])
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        def dfs(x, y):
            if board[x][y] != 'E':
                return

            # Count adjacent mines
            count = 0
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'M':
                    count += 1

            if count > 0:
                board[x][y] = str(count)
            else:
                board[x][y] = 'B'
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n:
                        dfs(nx, ny)

        x, y = click

        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            dfs(x, y)

        return board

# LeetCode 529: Minesweeper
# Explanation:
# 1. We are given a 2D board with 'M' (mine), 'E' (empty), 'B' (blank revealed), and numbers.
# 2. Clicking a cell reveals it:
#    - If it's a mine ('M'), change it to 'X' (game over).
#    - If it's empty ('E'):
#        - Count adjacent mines.
#        - If count > 0, replace with count.
#        - If count == 0, replace with 'B' and recursively reveal neighbors.
# 3. Use DFS or BFS to reveal cells.

# Methods Used:
# - DFS (Optimal)
# - BFS Alternative

# Time Complexity:
# - O(m*n), all cells can be visited

# Space Complexity:
# - O(m*n) for recursion stack in worst case


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


# -------------------------------------------------------
# Examples (Including Edge Cases)
# -------------------------------------------------------

# Example 1
board1 = [['E','E','E','E','E'],
          ['E','E','M','E','E'],
          ['E','E','E','E','E'],
          ['E','E','E','E','E']]
click1 = [3,0]
res1 = Solution().updateBoard(board1, click1)
for row in res1:
    print(row)
# Expected: reveal area around click with counts

# Example 2
board2 = [['B','1','E','1','B'],
          ['B','1','M','1','B'],
          ['B','1','1','1','B'],
          ['B','B','B','B','B']]
click2 = [1,2]
res2 = Solution().updateBoard(board2, click2)
for row in res2:
    print(row)
# Expected: clicked on mine -> 'X'

# Example 3 (Single cell mine)
board3 = [['M']]
click3 = [0,0]
print(Solution().updateBoard(board3, click3))
# [['X']]

# Example 4 (Single empty cell)
board4 = [['E']]
click4 = [0,0]
print(Solution().updateBoard(board4, click4))
# [['B']]

# Example 5 (Empty board)
board5 = []
click5 = [0,0]
print(Solution().updateBoard(board5, click5))
# []

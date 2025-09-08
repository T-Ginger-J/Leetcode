#O(1)
class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def is_valid(r, c, ch):
            for i in range(9):
                if board[r][i] == ch:  # row
                    return False
                if board[i][c] == ch:  # col
                    return False
                # 3x3 subgrid
                if board[(r//3)*3 + i//3][(c//3)*3 + i%3] == ch:
                    return False
            return True

        def backtrack():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for ch in map(str, range(1, 10)):
                            if is_valid(i, j, ch):
                                board[i][j] = ch
                                if backtrack():
                                    return True
                                board[i][j] = '.'  # backtrack
                        return False
            return True

        backtrack()


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

    def solveSudokuBitmask(self, board: list[list[str]]) -> None:
        """
        Optimized Backtracking with Bitmasks
        """

        # Track used digits with bitmasks
        row_mask = [0] * 9
        col_mask = [0] * 9
        box_mask = [0] * 9
        empties = []

        def box_index(r, c):
            return (r // 3) * 3 + (c // 3)

        # Initialize masks and list of empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empties.append((r, c))
                else:
                    d = int(board[r][c])
                    bit = 1 << (d - 1)
                    row_mask[r] |= bit
                    col_mask[c] |= bit
                    box_mask[box_index(r, c)] |= bit

        def backtrack(idx=0):
            if idx == len(empties):
                return True

            r, c = empties[idx]
            b = box_index(r, c)
            # Get available digits using bitmask trick
            available = ~(row_mask[r] | col_mask[c] | box_mask[b]) & 0x1FF

            while available:
                bit = available & -available  # lowest set bit
                d = (bit.bit_length() - 1) + 1  # digit
                board[r][c] = str(d)

                # Place digit
                row_mask[r] |= bit
                col_mask[c] |= bit
                box_mask[b] |= bit

                if backtrack(idx + 1):
                    return True

                # Backtrack
                row_mask[r] ^= bit
                col_mask[c] ^= bit
                box_mask[b] ^= bit
                board[r][c] = '.'

                available &= available - 1  # remove lowest set bit

            return False

        backtrack()


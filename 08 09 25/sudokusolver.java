class Solution {
    private int[] rowMask = new int[9];
    private int[] colMask = new int[9];
    private int[] boxMask = new int[9];
    private List<int[]> empties = new ArrayList<>();

    public void solveSudoku(char[][] board) {
        // Initialize masks and list of empty cells
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') {
                    empties.add(new int[]{r, c});
                } else {
                    int d = board[r][c] - '0';
                    int bit = 1 << (d - 1);
                    rowMask[r] |= bit;
                    colMask[c] |= bit;
                    boxMask[boxIndex(r, c)] |= bit;
                }
            }
        }
        backtrack(board, 0);
    }

    private boolean backtrack(char[][] board, int idx) {
        if (idx == empties.size()) return true;

        int r = empties.get(idx)[0];
        int c = empties.get(idx)[1];
        int b = boxIndex(r, c);

        // Available digits
        int available = ~(rowMask[r] | colMask[c] | boxMask[b]) & 0x1FF;

        while (available != 0) {
            int bit = available & -available; // lowest set bit
            int d = Integer.numberOfTrailingZeros(bit) + 1;

            // Place digit
            board[r][c] = (char) ('0' + d);
            rowMask[r] |= bit;
            colMask[c] |= bit;
            boxMask[b] |= bit;

            if (backtrack(board, idx + 1)) return true;

            // Undo
            rowMask[r] ^= bit;
            colMask[c] ^= bit;
            boxMask[b] ^= bit;
            board[r][c] = '.';

            available &= available - 1; // remove lowest set bit
        }
        return false;
    }

    private int boxIndex(int r, int c) {
        return (r / 3) * 3 + (c / 3);
    }
}

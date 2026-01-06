impl Solution {
    pub fn solve_sudoku(board: &mut Vec<Vec<char>>) {
        fn is_valid(board: &Vec<Vec<char>>, row: usize, col: usize, ch: char) -> bool {
            for i in 0..9 {
                // Check row
                if board[row][i] == ch {
                    return false;
                }
                // Check column
                if board[i][col] == ch {
                    return false;
                }
                // Check 3x3 subgrid
                let r = (row / 3) * 3 + i / 3;
                let c = (col / 3) * 3 + i % 3;
                if board[r][c] == ch {
                    return false;
                }
            }
            true
        }

        fn backtrack(board: &mut Vec<Vec<char>>) -> bool {
            for r in 0..9 {
                for c in 0..9 {
                    if board[r][c] == '.' {
                        for ch in '1'..='9' {
                            if is_valid(board, r, c, ch) {
                                board[r][c] = ch;
                                if backtrack(board) {
                                    return true;
                                }
                                board[r][c] = '.'; // backtrack
                            }
                        }
                        return false;
                    }
                }
            }
            true
        }

        backtrack(board);
    }
}

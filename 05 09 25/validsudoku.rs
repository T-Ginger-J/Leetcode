struct Solution;

impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        let mut rows = vec![std::collections::HashSet::new(); 9];
        let mut cols = vec![std::collections::HashSet::new(); 9];
        let mut boxes = vec![std::collections::HashSet::new(); 9];

        for i in 0..9 {
            for j in 0..9 {
                let c = board[i][j];
                if c != '.' {
                    let box_index = (i / 3) * 3 + (j / 3);
                    if rows[i].contains(&c) || cols[j].contains(&c) || boxes[box_index].contains(&c) {
                        return false;
                    }
                    rows[i].insert(c);
                    cols[j].insert(c);
                    boxes[box_index].insert(c);
                }
            }
        }

        true
    }
}


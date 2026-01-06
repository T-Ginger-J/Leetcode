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

fn main() {
    let board = vec![
        vec!['5','3','.','.','7','.','.','.','.'],
        vec!['6','.','.','1','9','5','.','.','.'],
        vec!['.','9','8','.','.','.','.','6','.'],
        vec!['8','.','.','.','6','.','.','.','3'],
        vec!['4','.','.','8','.','3','.','.','1'],
        vec!['7','.','.','.','2','.','.','.','6'],
        vec!['.','6','.','.','.','.','2','8','.'],
        vec!['.','.','.','4','1','9','.','.','5'],
        vec!['.','.','.','.','8','.','.','7','9'],
    ];

    println!("{}", Solution::is_valid_sudoku(board)); // Output: true
}

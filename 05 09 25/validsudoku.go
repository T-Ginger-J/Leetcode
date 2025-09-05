package main

import "fmt"

func isValidSudoku(board [][]byte) bool {
    rows := make([]map[byte]bool, 9)
    cols := make([]map[byte]bool, 9)
    boxes := make([]map[byte]bool, 9)

    for i := 0; i < 9; i++ {
        rows[i] = make(map[byte]bool)
        cols[i] = make(map[byte]bool)
        boxes[i] = make(map[byte]bool)
    }

    for i := 0; i < 9; i++ {
        for j := 0; j < 9; j++ {
            c := board[i][j]
            if c != '.' {
                boxIndex := (i/3)*3 + j/3
                if rows[i][c] || cols[j][c] || boxes[boxIndex][c] {
                    return false
                }
                rows[i][c] = true
                cols[j][c] = true
                boxes[boxIndex][c] = true
            }
        }
    }

    return true
}

func main() {
    board := [][]byte{
        {'5','3','.','.','7','.','.','.','.'},
        {'6','.','.','1','9','5','.','.','.'},
        {'.','9','8','.','.','.','.','6','.'},
        {'8','.','.','.','6','.','.','.','3'},
        {'4','.','.','8','.','3','.','.','1'},
        {'7','.','.','.','2','.','.','.','6'},
        {'.','6','.','.','.','.','2','8','.'},
        {'.','.','.','4','1','9','.','.','5'},
        {'.','.','.','.','8','.','.','7','9'},
    }

    fmt.Println(isValidSudoku(board)) // Output: true
}

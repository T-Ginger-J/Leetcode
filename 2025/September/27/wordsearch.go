// LeetCode 79: Word Search
// Explanation:
// 1. DFS with backtracking.
// 2. Explore 4 directions, marking visited temporarily.
// Time Complexity: O(m * n * 4^L)
// Space Complexity: O(L)

package main

import "fmt"

type Solution struct{}

func (s Solution) Exist(board [][]byte, word string) bool {
    rows, cols := len(board), len(board[0])
    
    var dfs func(r, c, idx int) bool
    dfs = func(r, c, idx int) bool {
        if idx == len(word) {
            return true
        }
        if r < 0 || r >= rows || c < 0 || c >= cols {
            return false
        }
        if board[r][c] != word[idx] {
            return false
        }
        
        temp := board[r][c]
        board[r][c] = '#'
        res := dfs(r+1, c, idx+1) || dfs(r-1, c, idx+1) || dfs(r, c+1, idx+1) || dfs(r, c-1, idx+1)
        board[r][c] = temp
        return res
    }
    
    for r := 0; r < rows; r++ {
        for c := 0; c < cols; c++ {
            if dfs(r, c, 0) {
                return true
            }
        }
    }
    return false
}

// Example usage:
func main() {
    sol := Solution{}
    board := [][]byte{
        {'A', 'B', 'C', 'E'},
        {'S', 'F', 'C', 'S'},
        {'A', 'D', 'E', 'E'},
    }
    fmt.Println(sol.Exist(board, "ABCCED")) // true
    fmt.Println(sol.Exist(board, "SEE"))    // true
    fmt.Println(sol.Exist(board, "ABCB"))   // false
}

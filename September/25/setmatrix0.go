// LeetCode 73: Set Matrix Zeroes
// Explanation:
// 1. Record which rows and cols must be zeroed.
// 2. Modify in-place.
// Time Complexity: O(m*n)
// Space Complexity: O(m + n)

package main

import "fmt"

type Solution struct{}

func (Solution) setZeroes(matrix [][]int) {
    m, n := len(matrix), len(matrix[0])
    rows := make([]bool, m)
    cols := make([]bool, n)

    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if matrix[i][j] == 0 {
                rows[i] = true
                cols[j] = true
            }
        }
    }

    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            if rows[i] || cols[j] {
                matrix[i][j] = 0
            }
        }
    }
}

// Example usage:
func main() {
    sol := Solution{}
    mat := [][]int{{1, 1, 1}, {1, 0, 1}, {1, 1, 1}}
    sol.setZeroes(mat)
    fmt.Println(mat) // [[1 0 1] [0 0 0] [1 0 1]]
}

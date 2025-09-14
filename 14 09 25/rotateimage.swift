//O(n^2)
class Solution {
    func rotate(_ matrix: inout [[Int]]) {
        let n = matrix.count
        
        // Step 1: Transpose the matrix
        for i in 0..<n {
            for j in i..<n {
                let temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
            }
        }
        
        // Step 2: Reverse each row
        for i in 0..<n {
            matrix[i].reverse()
        }
    }
}


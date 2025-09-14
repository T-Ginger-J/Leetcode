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

var matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

let sol = Solution()
sol.rotate(&matrix)
print(matrix)
// [[7,4,1],[8,5,2],[9,6,3]]

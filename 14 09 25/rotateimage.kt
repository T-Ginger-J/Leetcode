class Solution {
    fun rotate(matrix: Array<IntArray>) {
        val n = matrix.size

        // Step 1: Transpose the matrix
        for (i in 0 until n) {
            for (j in i until n) {
                val temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
            }
        }

        // Step 2: Reverse each row
        for (i in 0 until n) {
            matrix[i].reverse()
        }
    }
}

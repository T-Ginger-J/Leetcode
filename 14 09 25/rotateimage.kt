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
    fun main() {
    val matrix = arrayOf(
        intArrayOf(1,2,3),
        intArrayOf(4,5,6),
        intArrayOf(7,8,9)
    )

    val sol = Solution()
    sol.rotate(matrix)

    matrix.forEach { println(it.joinToString(",")) }
    // Output:
    // 7,4,1
    // 8,5,2
    // 9,6,3
}

}

//O(1)
object Solution {
    def isValidSudoku(board: Array[Array[Char]]): Boolean = {
        val rows = Array.fill(9)(scala.collection.mutable.Set[Char]())
        val cols = Array.fill(9)(scala.collection.mutable.Set[Char]())
        val boxes = Array.fill(9)(scala.collection.mutable.Set[Char]())

        for (i <- 0 until 9) {
            for (j <- 0 until 9) {
                val c = board(i)(j)
                if (c != '.') {
                    val boxIndex = (i / 3) * 3 + (j / 3)
                    if (rows(i).contains(c) || cols(j).contains(c) || boxes(boxIndex).contains(c)) {
                        return false
                    }
                    rows(i).add(c)
                    cols(j).add(c)
                    boxes(boxIndex).add(c)
                }
            }
        }
        true
    }

    def main(args: Array[String]): Unit = {
        val board = Array(
            Array('5','3','.','.','7','.','.','.','.'),
            Array('6','.','.','1','9','5','.','.','.'),
            Array('.','9','8','.','.','.','.','6','.'),
            Array('8','.','.','.','6','.','.','.','3'),
            Array('4','.','.','8','.','3','.','.','1'),
            Array('7','.','.','.','2','.','.','.','6'),
            Array('.','6','.','.','.','.','2','8','.'),
            Array('.','.','.','4','1','9','.','.','5'),
            Array('.','.','.','.','8','.','.','7','9')
        )

        println(isValidSudoku(board)) // Output: true
    }
}

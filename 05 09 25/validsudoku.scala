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

}

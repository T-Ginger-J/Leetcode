class Solution {
    func solveNQueens(_ n: Int) -> [[String]] {
        var res = [[String]]()
        var board = Array(repeating: Array(repeating: ".", count: n), count: n)
        
        func backtrack(_ row: Int, _ cols: inout Set<Int>, _ diag1: inout Set<Int>, _ diag2: inout Set<Int>) {
            if row == n {
                res.append(board.map { $0.joined() })
                return
            }
            
            for c in 0..<n {
                if cols.contains(c) || diag1.contains(row - c) || diag2.contains(row + c) {
                    continue
                }
                board[row][c] = "Q"
                cols.insert(c)
                diag1.insert(row - c)
                diag2.insert(row + c)
                
                backtrack(row + 1, &cols, &diag1, &diag2)
                
                board[row][c] = "."
                cols.remove(c)
                diag1.remove(row - c)
                diag2.remove(row + c)
            }
        }
        
        var cols = Set<Int>()
        var diag1 = Set<Int>()
        var diag2 = Set<Int>()
        backtrack(0, &cols, &diag1, &diag2)
        return res
    }
}


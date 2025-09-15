class Solution:
    def solveNQueens(self, n: int):
        res = []
        board = [["."] * n for _ in range(n)]
        cols = set()
        diag1 = set()  # r - c
        diag2 = set()  # r + c

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            for c in range(n):
                if c in cols or (r-c) in diag1 or (r+c) in diag2:
                    continue
                board[r][c] = "Q"
                cols.add(c); diag1.add(r-c); diag2.add(r+c)
                backtrack(r+1)
                board[r][c] = "."
                cols.remove(c); diag1.remove(r-c); diag2.remove(r+c)

        backtrack(0)
        return res

    def solveNQueensRecursive(self, n):
        def f(r=0, cols=set(), d1=set(), d2=set(), board=[]):
            if r==n: return [["".join(row) for row in board]]
            return [res for c in range(n) if c not in cols and r-c not in d1 and r+c not in d2
                    for res in f(r+1, cols|{c}, d1|{r-c}, d2|{r+c}, board+[["."]*c+["Q"]+["."]*(n-c-1)])]
        return f()


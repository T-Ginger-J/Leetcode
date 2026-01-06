# LeetCode 73: Set Matrix Zeroes
# Explanation:
# 1. Traverse matrix and record which rows/cols must be zeroed.
# 2. Iterate again to set corresponding rows and cols to 0.
# Time Complexity: O(m*n)
# Space Complexity: O(m + n)

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        rows, cols = set(), set()
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)

        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 05

    def setZeroesSkip(self, matrix: list[list[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0

    setZeroesOneLine=lambda s,m:[m.__setitem__(i,[0]*len(m[0])) for i in range(len(m)) for j in range(len(m[0])) if not m[i][j]]        

# Example usage:
# sol = Solution()
# mat = [[1,1,1],[1,0,1],[1,1,1]]
# sol.setZeroes(mat)
# print(mat)  # [[1,0,1],[0,0,0],[1,0,1]]

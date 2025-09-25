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
    setZeroesOneLine=lambda s,m:[m.__setitem__(i,[0]*len(m[0])) for i in range(len(m)) for j in range(len(m[0])) if not m[i][j]]        

# Example usage:
# sol = Solution()
# mat = [[1,1,1],[1,0,1],[1,1,1]]
# sol.setZeroes(mat)
# print(mat)  # [[1,0,1],[0,0,0],[1,0,1]]

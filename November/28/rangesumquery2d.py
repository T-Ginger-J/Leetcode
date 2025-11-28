# LeetCode 304: Range Sum Query 2D - Immutable
# Explanation:
# 1. Precompute 2D prefix sums.
# 2. prefix[i+1][j+1] = sum of elements from (0,0) to (i,j).
# 3. sumRegion(row1, col1, row2, col2) = prefix[row2+1][col2+1] - prefix[row1][col2+1] - prefix[row2+1][col1] + prefix[row1][col1]
# Time Complexity: O(m*n) preprocessing, O(1) per query
# Space Complexity: O(m*n) for prefix sum array

class NumMatrix:

    def __init__(self, matrix):
        if not matrix or not matrix[0]: 
            self.prefix = [[0]]
            return
        m, n = len(matrix), len(matrix[0])
        self.prefix = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                self.prefix[i+1][j+1] = matrix[i][j] + self.prefix[i][j+1] + self.prefix[i+1][j] - self.prefix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        return self.prefix[row2+1][col2+1] - self.prefix[row1][col2+1] - self.prefix[row2+1][col1] + self.prefix[row1][col1]


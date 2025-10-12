# LeetCode 118: Pascal’s Triangle
# Explanation:
# 1. Build Pascal’s Triangle up to numRows.
# 2. Each row starts and ends with 1.
# 3. Each interior element = sum of two elements above it: row[i] = prev[i-1] + prev[i].
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)

class Solution:
    def generate(self, numRows: int):
        triangle = []
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)
        return triangle

    def generateOneLine(self, n):
        return [[1] * (i + 1) if i < 2 else [1] + [a + b for a, b in zip(r[:-1], r[1:])] + [1] for i, r in enumerate([[1]] * n)]


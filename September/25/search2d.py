# LeetCode 74: Search a 2D Matrix
# Explanation:
# 1. Treat matrix as a flattened sorted array of length m*n.
# 2. Perform binary search using index conversion (mid // n, mid % n).
# Time Complexity: O(log(m*n))
# Space Complexity: O(1)

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = (left + right) // 2
            val = matrix[mid // n][mid % n]
            if val == target:
                return True
            elif val < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
    searchMatrixOneLine=lambda s,m,t:any(t in r for r in m)

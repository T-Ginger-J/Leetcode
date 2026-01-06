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
    
    def searchMatrixBinary(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        top, bot = 0, m - 1

        while top <= bot:
            row = (top + bot) // 2
            if target < matrix[row][0]:
                bot = row - 1
            elif target > matrix[row][-1]:
                top = row + 1
            else:
                break
        else:
            return False

        row = (top + bot) // 2
        l, r = 0, n - 1
        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
    
    searchMatrixOneLine=lambda s,m,t:any(t in r for r in m)

# Example usage:
# sol = Solution()
# print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))   # True
# print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))  # False

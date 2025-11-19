# LeetCode 240: Search a 2D Matrix II
# Explanation:
# Matrix is sorted:
#   - each row left → right
#   - each column top → bottom
#
# Start from top-right:
#   - If target == value → found
#   - If target < value → move left
#   - If target > value → move down
#
# This works because each move eliminates a full row or column.
#
# Time Complexity: O(m + n)
# Space Complexity: O(1)

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        r, c = 0, len(matrix[0]) - 1

        while r < len(matrix) and c >= 0:
            if matrix[r][c] == target:
                return True
            elif matrix[r][c] > target:
                c -= 1
            else:
                r += 1

        return False

# Example usage:
# sol = Solution()
# print(sol.searchMatrix([[1,4,7],[2,5,8],[3,6,9]], 5))   # True
# print(sol.searchMatrix([[1,2],[3,4]], 10))              # False

# LeetCode 566: Reshape the Matrix
# Explanation:
# 1. Given a 2D matrix mat of size m x n and integers r and c, reshape the matrix to size r x c while keeping the original data row-wise.
# 2. Approach:
#    - Check if r*c == m*n, otherwise return original matrix.
#    - Flatten the matrix into a list and rebuild in new dimensions.
#    - Can also fill new matrix directly using index arithmetic.
# 3. Time Complexity: O(m*n)
# 4. Space Complexity: O(m*n) (or O(1) if reshape in-place is allowed using index mapping)

from typing import List

class Solution:

    # -------------------------------------------------------
    # Method 1: Flatten and rebuild
    # -------------------------------------------------------
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m*n != r*c:
            return mat
        flat = [num for row in mat for num in row]
        return [flat[i*c:(i+1)*c] for i in range(r)]


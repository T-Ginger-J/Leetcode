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

    # -------------------------------------------------------
    # Method 2: Direct index mapping without extra list
    # -------------------------------------------------------
    def matrixReshapeDirect(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        if m*n != r*c:
            return mat
        res = [[0]*c for _ in range(r)]
        for i in range(m*n):
            res[i//c][i%c] = mat[i//n][i%n]
        return res


# -------------------------------------------------------
# Examples & Edge Cases
# -------------------------------------------------------

sol = Solution()

# Example 1
mat1 = [[1,2],[3,4]]
r1, c1 = 1,4
print(sol.matrixReshape(mat1, r1, c1))           # [[1,2,3,4]]
print(sol.matrixReshapeDirect(mat1, r1, c1))    # [[1,2,3,4]]

# Example 2: same size, should return original
mat2 = [[1,2],[3,4]]
r2, c2 = 2,2
print(sol.matrixReshape(mat2, r2, c2))           # [[1,2],[3,4]]

# Example 3: impossible reshape
mat3 = [[1,2],[3,4]]
r3, c3 = 3,2
print(sol.matrixReshape(mat3, r3, c3))           # [[1,2],[3,4]]

# Example 4: 1x1 matrix
mat4 = [[5]]
r4, c4 = 1,1
print(sol.matrixReshape(mat4, r4, c4))           # [[5]]

# Example 5: larger reshape
mat5 = [[1,2,3],[4,5,6]]
r5, c5 = 3,2
print(sol.matrixReshapeDirect(mat5, r5, c5))     # [[1,2],[3,4],[5,6]]

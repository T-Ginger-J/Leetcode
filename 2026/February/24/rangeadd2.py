# LeetCode 598: Range Addition II
# Explanation:
# 1. We start with an m x n matrix initialized with 0.
# 2. Each operation [a, b] increments all cells in submatrix [0..a-1][0..b-1].
# 3. The maximum value will appear in the overlapping region
#    of all operations.
# 4. So we only need:
#       min_row = min(a for each op)
#       min_col = min(b for each op)
# 5. Result = min_row * min_col
# 6. If ops is empty, all cells are equal → m * n.
# 7. Time Complexity: O(k), k = len(ops)
# 8. Space Complexity: O(1)

from typing import List


class Solution:

    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:

        # No operations → whole matrix is max
        if not ops:
            return m * n

        min_row = m
        min_col = n

        for a, b in ops:
            min_row = min(min_row, a)
            min_col = min(min_col, b)

        return min_row * min_col


# -------------------------------------------------------
# Examples & Edge Cases
# -------------------------------------------------------

sol = Solution()

# Example 1
print(sol.maxCount(3, 3, [[2,2],[3,3]]))   # 4

# Example 2: No ops
print(sol.maxCount(3, 3, []))             # 9

# Example 3: Single op
print(sol.maxCount(4, 5, [[2,3]]))         # 6

# Example 4: Full matrix
print(sol.maxCount(5, 5, [[5,5]]))         # 25

# Example 5: Different overlaps
print(sol.maxCount(5, 5, [[4,4],[3,5],[5,3]]))  # 9

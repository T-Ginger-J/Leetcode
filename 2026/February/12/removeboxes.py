# LeetCode 546: Remove Boxes
# Explanation:
# 1. Given an array of boxes with colors represented by numbers, remove them to maximize points.
# 2. Removing k consecutive boxes of the same color gives k*k points.
# 3. After removal, remaining boxes shift to fill the gap.
# 4. Use DP with memoization: dp(l, r, k) = max points for boxes[l:r+1] with k boxes of same color as boxes[r] contiguous to the right.

# Methods Used:
# - 3D DP with memoization (l, r, k)
# - Recursively try removing last boxes or merging same-color boxes

# Time Complexity:
# - O(n^3) in worst case, n = len(boxes)

# Space Complexity:
# - O(n^3) for memoization


from typing import List
from functools import lru_cache


class Solution:

    # -------------------------------------------------------
    # Method 1: 3D DP with Memoization
    # -------------------------------------------------------
    def removeBoxes(self, boxes: List[int]) -> int:

        n = len(boxes)

        @lru_cache(None)
        def dp(l: int, r: int, k: int) -> int:
            if l > r:
                return 0

            # Optimize: merge boxes of same color at the end
            while r > l and boxes[r] == boxes[r-1]:
                r -= 1
                k += 1

            res = dp(l, r-1, 0) + (k+1)*(k+1)

            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    res = max(res, dp(l, i, k+1) + dp(i+1, r-1, 0))

            return res

        return dp(0, n-1, 0)


# -------------------------------------------------------
# Examples (Including Edge Cases)
# -------------------------------------------------------

# Example 1
boxes1 = [1,3,2,2,2,3,4,3,1]
print(Solution().removeBoxes(boxes1))  # 23

# Example 2 (All same)
boxes2 = [1,1,1,1]
print(Solution().removeBoxes(boxes2))  # 16 (4*4)

# Example 3 (All unique)
boxes3 = [1,2,3,4]
print(Solution().removeBoxes(boxes3))  # 4 (1*1 + 1*1 + 1*1 + 1*1)

# Example 4 (Empty)
boxes4 = []
print(Solution().removeBoxes(boxes4))  # 0

# Example 5 (Two colors alternating)
boxes5 = [1,2,1,2,1]
print(Solution().removeBoxes(boxes5))

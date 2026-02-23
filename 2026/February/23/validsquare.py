# LeetCode 593: Valid Square
# Explanation:
# 1. We are given 4 points in 2D space.
# 2. They form a valid square if:
#    - All four sides are equal and non-zero.
#    - Both diagonals are equal.
# 3. Approach:
#    - Compute all pairwise squared distances (6 total).
#    - In a square:
#         • 4 smallest distances are equal (sides)
#         • 2 largest distances are equal (diagonals)
#    - Use squared distance to avoid floating point errors.
# 4. Time Complexity: O(1) (constant, only 6 distances)
# 5. Space Complexity: O(1)

from typing import List


class Solution:

    def validSquare(self,
                    p1: List[int],
                    p2: List[int],
                    p3: List[int],
                    p4: List[int]) -> bool:

        def dist(a, b):
            return (a[0]-b[0])**2 + (a[1]-b[1])**2

        points = [p1, p2, p3, p4]

        dists = []

        # Compute all pairwise distances
        for i in range(4):
            for j in range(i+1, 4):
                dists.append(dist(points[i], points[j]))

        dists.sort()

        # Conditions for square:
        # - smallest distance > 0 (no overlapping points)
        # - first 4 equal (sides)
        # - last 2 equal (diagonals)
        return (
            dists[0] > 0 and
            dists[0] == dists[1] == dists[2] == dists[3] and
            dists[4] == dists[5]
        )


# -------------------------------------------------------
# Examples & Edge Cases
# -------------------------------------------------------

sol = Solution()

# Example 1: Valid square
print(sol.validSquare([0, 0], [1, 1], [1, 0], [0, 1]))   # True

# Example 2: Rectangle (not square)
print(sol.validSquare([0, 0], [2, 0], [2, 1], [0, 1]))   # False

# Example 3: Overlapping points
print(sol.validSquare([0, 0], [0, 0], [1, 1], [1, 0]))   # False

# Example 4: Rotated square
print(sol.validSquare([1, 1], [2, 2], [3, 1], [2, 0]))   # True

# Example 5: Random points
print(sol.validSquare([0, 0], [1, 2], [2, 1], [3, 3]))   # False

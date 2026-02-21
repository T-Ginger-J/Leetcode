# LeetCode 587: Erect the Fence (Convex Hull)
# Explanation:
# 1. Given points in 2D, return the smallest convex polygon (fence) enclosing all points.
# 2. Approach:
#    - Use the Monotone Chain algorithm (variant of Graham Scan):
#       a. Sort points lexicographically by x then y.
#       b. Build upper hull from left to right:
#          - Keep popping last point if new point makes a clockwise turn.
#       c. Build lower hull from right to left using same logic.
#       d. Merge hulls and remove duplicates.
#    - This approach handles collinear points on the boundary.
# 3. Time Complexity: O(n log n) due to sorting
# 4. Space Complexity: O(n) for storing hull points

from typing import List

class Solution:
    def outerTrees(self, points: List[List[int]]) -> List[List[int]]:

        if len(points) <= 3:
            return points

        # Cross product of vectors AB x AC
        def cross(A, B, C):
            return (B[0]-A[0])*(C[1]-A[1]) - (B[1]-A[1])*(C[0]-A[0])

        # Sort points lexicographically
        points.sort()
        
        # Build upper hull
        upper = []
        for p in points:
            while len(upper) >= 2 and cross(upper[-2], upper[-1], p) > 0:
                upper.pop()
            upper.append(p)
        
        # Build lower hull
        lower = []
        for p in reversed(points):
            while len(lower) >= 2 and cross(lower[-2], lower[-1], p) > 0:
                lower.pop()
            lower.append(p)

        # Merge and remove duplicates
        full_hull = upper[:-1] + lower[:-1]
        # Remove duplicates
        unique_hull = list(map(list, set(map(tuple, full_hull))))
        return unique_hull


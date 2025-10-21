# LeetCode 149: Max Points on a Line (Optimized)
# Explanation:
# 1. Use float slope representation to simplify slope calculation.
# 2. Handle vertical lines with "inf" and horizontal lines with slope 0.
# 3. Faster due to simpler hashing.
# Time Complexity: O(n²)
# Space Complexity: O(n)

class Solution:
    def maxPoints(self, points):
        if len(points) <= 2:
            return len(points)
        max_points = 0
        for i, (x1, y1) in enumerate(points):
            slopes = {}
            duplicates = 1
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                if x1 == x2 and y1 == y2:
                    duplicates += 1
                elif x1 == x2:
                    slopes['inf'] = slopes.get('inf', 0) + 1
                else:
                    slope = (y2 - y1) / (x2 - x1)
                    slopes[slope] = slopes.get(slope, 0) + 1
            max_points = max(max_points, duplicates + max(slopes.values(), default=0))
        return max_points

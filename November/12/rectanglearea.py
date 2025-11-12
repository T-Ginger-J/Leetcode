# LeetCode 223: Rectangle Area
# Explanation:
# 1. Compute area of each rectangle separately.
# 2. Find overlap width = max(0, min(ax2, bx2) - max(ax1, bx1)).
# 3. Find overlap height = max(0, min(ay2, by2) - max(ay1, by1)).
# 4. Subtract overlapping area once.
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int,
                    bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1)

        overlap_width = max(0, min(ax2, bx2) - max(ax1, bx1))
        overlap_height = max(0, min(ay2, by2) - max(ay1, by1))
        overlap_area = overlap_width * overlap_height

        return area_a + area_b - overlap_area
    
    def computeAreaLambda(self, ax1, ay1, ax2, ay2, bx1, by1, bx2, by2):
        area = lambda x1, y1, x2, y2: (x2 - x1) * (y2 - y1)
        overlap = lambda a1, a2, b1, b2: max(0, min(a2, b2) - max(a1, b1))
        return area(ax1, ay1, ax2, ay2) + area(bx1, by1, bx2, by2) - \
               overlap(ax1, ax2, bx1, bx2) * overlap(ay1, ay2, by1, by2)



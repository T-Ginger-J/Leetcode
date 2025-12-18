# LeetCode 391: Perfect Rectangle
# Explanation:
# 1. Sum areas of all small rectangles
# 2. Track corners using a set
# 3. Check total area and final corners
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def isRectangleCover(self, rectangles: list[list[int]]) -> bool:
        min_x = min_y = float('inf')
        max_x = max_y = float('-inf')
        corners = set()
        total_area = 0

        for x1, y1, x2, y2 in rectangles:
            min_x = min(min_x, x1)
            min_y = min(min_y, y1)
            max_x = max(max_x, x2)
            max_y = max(max_y, y2)
            total_area += (x2 - x1) * (y2 - y1)

            for corner in [(x1,y1), (x1,y2), (x2,y1), (x2,y2)]:
                if corner in corners:
                    corners.remove(corner)
                else:
                    corners.add(corner)

        if len(corners) != 4 or (min_x,min_y) not in corners or (min_x,max_y) not in corners \
           or (max_x,min_y) not in corners or (max_x,max_y) not in corners:
            return False

        return total_area == (max_x - min_x) * (max_y - min_y)

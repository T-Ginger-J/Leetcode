# LeetCode 497: Random Point in Non-overlapping Rectangles
# Explanation:
# Given a list of non-overlapping axis-aligned rectangles, randomly pick
# an integer point inside the rectangles uniformly.
#
# Method 1: Prefix Sum of Area + Binary Search
# - Compute the number of integer points in each rectangle.
# - Build prefix sum array of point counts.
# - Pick a random integer r in total points, use binary search to find rectangle.
# - Randomly pick a point inside that rectangle.
#
# Time Complexity: O(log n) per pick
# Space Complexity: O(n)

from typing import List
import random
import bisect

class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weights = []
        total = 0
        for x1, y1, x2, y2 in rects:
            cnt = (x2 - x1 + 1) * (y2 - y1 + 1)
            total += cnt
            self.weights.append(total)

    def pick(self) -> List[int]:
        r = random.randint(1, self.weights[-1])
        idx = bisect.bisect_left(self.weights, r)
        x1, y1, x2, y2 = self.rects[idx]
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)
        return [x, y]


# Alternate Python Solution: Flatten Points (not space efficient)
# - Store all points in a list and pick randomly
# - Only useful for small rectangles

class SolutionBrute:
    def __init__(self, rects: List[List[int]]):
        self.points = []
        for x1, y1, x2, y2 in rects:
            for x in range(x1, x2+1):
                for y in range(y1, y2+1):
                    self.points.append([x, y])

    def pick(self) -> List[int]:
        return random.choice(self.points)


# Additional Examples (Edge Cases and Non-LeetCode Examples)

# Example 1: Single rectangle
sol = Solution([[1,1,2,2]])
print(sol.pick())  # Expected: any point [1,1],[1,2],[2,1],[2,2]

# Example 2: Multiple rectangles
sol2 = Solution([[1,1,1,1],[2,2,3,3]])
print(sol2.pick())  # Expected: points in either rectangle

# Example 3: Rectangles with one row/column
sol3 = Solution([[0,0,0,5],[2,2,2,2]])
print(sol3.pick())  # Expected: points along vertical line or single point

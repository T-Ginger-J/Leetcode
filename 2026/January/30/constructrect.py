# LeetCode 492: Construct the Rectangle
# Explanation:
# Given an area, find the dimensions L and W such that:
# 1. L * W == area
# 2. L >= W
# 3. L - W is minimized
#
# Method 1: Square Root Search (Optimal)
# - Iterate W from sqrt(area) down to 1.
# - Return the first W that divides area evenly.
#
# Time Complexity: O(sqrt(n))
# Space Complexity: O(1)

from typing import List
import math

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        w = int(math.sqrt(area))
        while area % w != 0:
            w -= 1
        return [area // w, w]


# Alternate Python Solution: Brute Force Up to sqrt(area)
# - Same as above, written slightly differently.

class SolutionBrute:
    def constructRectangle(self, area: int) -> List[int]:
        for w in range(int(area ** 0.5), 0, -1):
            if area % w == 0:
                return [area // w, w]
        return [area,1]  # fallback, though unreachable


# Additional Examples (Edge Cases and Non-LeetCode Examples)


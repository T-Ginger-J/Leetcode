# LeetCode 463: Island Perimeter
# Explanation:
# Given a grid where 1 represents land and 0 represents water,
# compute the perimeter of the island.
#
# Method 1: Count Land and Shared Edges (Optimal)
# - Each land cell contributes 4 edges.
# - For each adjacent land neighbor, subtract 2 (shared edge).
#
# Time Complexity: O(rows * cols)
# Space Complexity: O(1)

from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    perimeter += 4
                    if r > 0 and grid[r-1][c] == 1:
                        perimeter -= 2
                    if c > 0 and grid[r][c-1] == 1:
                        perimeter -= 2
        return perimeter


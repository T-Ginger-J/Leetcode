# LeetCode 554: Brick Wall
# Explanation:
# 1. Given a wall represented as a list of rows, where each row contains brick widths.
# 2. Find the minimum number of bricks crossed by a vertical line from top to bottom.
# 3. Approach:
#    - Count the positions of brick edges (excluding the rightmost edge).
#    - The vertical line crossing at the most frequent edge will cross the fewest bricks.
#    - Result = total rows - max frequency of edge positions.

# Time Complexity:
# - O(n), n = total number of bricks
# Space Complexity:
# - O(k), k = number of unique edge positions

from typing import List
from collections import defaultdict

class Solution:

    # -------------------------------------------------------
    # Method 1: Hash Map
    # -------------------------------------------------------
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_counts = defaultdict(int)
        for row in wall:
            edge = 0
            for brick in row[:-1]:  # skip last brick
                edge += brick
                edge_counts[edge] += 1
        max_edges = max(edge_counts.values(), default=0)
        return len(wall) - max_edges

    # -------------------------------------------------------
    # Method 2: Optimized single pass
    # -------------------------------------------------------
    def leastBricksOptimized(self, wall: List[List[int]]) -> int:
        count = {}
        for row in wall:
            s = 0
            for brick in row[:-1]:
                s += brick
                count[s] = count.get(s,0)+1
        return len(wall) - max(count.values(), default=0)

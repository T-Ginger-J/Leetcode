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

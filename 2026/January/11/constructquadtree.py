from typing import List

# Definition for a QuadTree node.
class Node:
    def __init__(self, val: bool, isLeaf: bool, 
                 topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(x0, y0, length):
            # Check if all values in this square are the same
            first_val = grid[x0][y0]
            all_same = True
            for i in range(x0, x0 + length):
                for j in range(y0, y0 + length):
                    if grid[i][j] != first_val:
                        all_same = False
                        break
                if not all_same:
                    break
            
            if all_same:
                return Node(val=bool(first_val), isLeaf=True)
            
            half = length // 2
            return Node(
                val=True,  # val can be arbitrary when not leaf
                isLeaf=False,
                topLeft=helper(x0, y0, half),
                topRight=helper(x0, y0 + half, half),
                bottomLeft=helper(x0 + half, y0, half),
                bottomRight=helper(x0 + half, y0 + half, half)
            )
        
        n = len(grid)
        return helper(0, 0, n)

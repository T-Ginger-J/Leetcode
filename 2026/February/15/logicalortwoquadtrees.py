# LeetCode 558: Logical OR of Two Quad-Trees
# Explanation:
# 1. Given two Quad-Trees representing n*n binary matrices, compute a Quad-Tree for the matrix resulting
#    from bitwise OR of the two matrices.
# 2. Approach:
#    - If either node is a leaf and its value is True (1), the result is True.
#    - If one node is leaf with False (0), result is the other node.
#    - If both are non-leaf, recursively compute OR for all four children.
#    - After recursion, check if all four children are leaf and have same value → merge into a leaf.
# 3. Time Complexity: O(n), n = number of nodes in the trees (each node visited once)
# 4. Space Complexity: O(h), h = height of the tree (recursive stack)

from typing import Optional

# Definition for a QuadTree node.
class Node:
    def __init__(self, val: bool, isLeaf: bool, 
                 topLeft: Optional['Node']=None, 
                 topRight: Optional['Node']=None, 
                 bottomLeft: Optional['Node']=None, 
                 bottomRight: Optional['Node']=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:

    # -------------------------------------------------------
    # Method 1: Recursive OR
    # -------------------------------------------------------
    def intersect(self, quadTree1: Node, quadTree2: Node) -> Node:
        if quadTree1.isLeaf:
            return Node(True, True) if quadTree1.val else quadTree2
        if quadTree2.isLeaf:
            return Node(True, True) if quadTree2.val else quadTree1
        
        topLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
        topRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
        bottomLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
        bottomRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)

        children = [topLeft, topRight, bottomLeft, bottomRight]

        # Merge children if all leaf with same value
        if all(c.isLeaf for c in children) and len(set(c.val for c in children)) == 1:
            return Node(topLeft.val, True)
        return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)


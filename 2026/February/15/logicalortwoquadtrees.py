from typing import Optional

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


from typing import Optional

class Solution:

    # -------------------------------------------------------
    # Method 1: DFS Post-order
    # -------------------------------------------------------
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.diameter = 0

        def height(node):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)

        height(root)
        return self.diameter


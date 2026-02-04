from collections import deque
from typing import Optional

class Solution:

    # -------------------------------------------------------
    # Method 1: BFS (Level Order Traversal)
    # -------------------------------------------------------
    def findBottomLeftValueBFS(self, root: Optional[TreeNode]) -> int:

        queue = deque([root])
        leftmost = root.val

        while queue:

            size = len(queue)

            for i in range(size):

                node = queue.popleft()

                # First node in each level is leftmost
                if i == 0:
                    leftmost = node.val

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

        return leftmost

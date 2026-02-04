# LeetCode 513: Find Bottom Left Tree Value
# Explanation:
# 1. Given a binary tree, find the value of the leftmost node in the last row.
# 2. The "bottom-left" value is the first node encountered from left to right
#    on the deepest level.
# 3. We can solve this using tree traversal.

# Methods Used:
# - Breadth-First Search (Level Order Traversal)
# - Depth-First Search (Preorder with Depth Tracking)

# Time Complexity:
# - Both methods: O(n), where n is the number of nodes.

# Space Complexity:
# - BFS: O(n) (queue in worst case)
# - DFS: O(h) recursion stack, where h is tree height (worst O(n))


from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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

    # -------------------------------------------------------
    # Method 2: DFS (Preorder with Depth Tracking)
    # -------------------------------------------------------
    def findBottomLeftValueDFS(self, root: Optional[TreeNode]) -> int:

        self.max_depth = -1
        self.answer = 0

        def dfs(node, depth):

            if not node:
                return

            # Visit left first to ensure leftmost priority
            if depth > self.max_depth:
                self.max_depth = depth
                self.answer = node.val

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)

        return self.answer


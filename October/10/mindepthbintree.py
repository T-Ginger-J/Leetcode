# LeetCode 111: Minimum Depth of Binary Tree
# Explanation:
# 1. The minimum depth is the number of nodes along the shortest path 
#    from the root node down to the nearest leaf node.
# 2. If a node has only one child, you must go down the non-null child.
# 3. Use DFS recursion to compute the minimum depth.
# Time Complexity: O(n) — each node is visited once.
# Space Complexity: O(h) — recursion stack height (worst case n, best case log n).

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.left:
            return 1 + self.minDepth(root.right)
        if not root.right:
            return 1 + self.minDepth(root.left)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

    def minDepthOptimized(self, root):
        if not root:
            return 0
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))


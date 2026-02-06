# LeetCode 515: Find Largest Value in Each Tree Row
# Explanation:
# 1. Given a binary tree, return a list of the largest value in each row (level).
# 2. Traverse the tree level by level (BFS) and record the max value per level.
# 3. Alternatively, DFS can track the max value at each depth.

# Methods Used:
# - BFS (Level Order Traversal)
# - DFS (Preorder with Depth Tracking)

# Time Complexity:
# - O(n), n = number of nodes

# Space Complexity:
# - BFS: O(n) for queue
# - DFS: O(h) recursion stack, h = tree height


from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # -------------------------------------------------------
    # Method 1: BFS
    # -------------------------------------------------------
    def largestValuesBFS(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:

            size = len(queue)
            max_val = float('-inf')

            for _ in range(size):
                node = queue.popleft()
                max_val = max(max_val, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(max_val)

        return res

    # -------------------------------------------------------
    # Method 2: DFS
    # -------------------------------------------------------
    def largestValuesDFS(self, root: Optional[TreeNode]) -> List[int]:

        res = []

        def dfs(node, depth):

            if not node:
                return

            if depth == len(res):
                res.append(node.val)
            else:
                res[depth] = max(res[depth], node.val)

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return res

    # -------------------------------------------------------
    # Default Method (BFS)
    # -------------------------------------------------------
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        return self.largestValuesBFS(root)


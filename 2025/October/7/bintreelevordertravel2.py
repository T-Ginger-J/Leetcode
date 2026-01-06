# LeetCode 107: Binary Tree Level Order Traversal II
# Explanation:
# 1. Perform a standard BFS level order traversal.
# 2. Collect nodes level by level.
# 3. Reverse the list of levels at the end to get bottom-up order.
# Time Complexity: O(n) — each node is visited once.
# Space Complexity: O(n) — queue and result storage.

from collections import deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue = deque([root])
        res = []
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(level)
        return res[::-1]

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))
print(Solution().levelOrderBottom(root))  # [[15, 7], [9, 20], [3]]

root = TreeNode(1)
print(Solution().levelOrderBottom(root))  # [[1]]

print(Solution().levelOrderBottom(None))  # []

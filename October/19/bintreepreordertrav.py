# LeetCode 144: Binary Tree Preorder Traversal
# Explanation:
# 1. Preorder traversal order: Root → Left → Right.
# 2. Use recursion to traverse each subtree.
# 3. Append node values in preorder sequence.
# Time Complexity: O(n)
# Space Complexity: O(n) for recursion stack

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def dfs(node):
            if not node:
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return res


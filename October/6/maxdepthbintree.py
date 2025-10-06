# LeetCode 104: Maximum Depth of Binary Tree
# Explanation:
# 1. The depth of a binary tree is the longest path from the root to a leaf.
# 2. Use recursion to find max depth of left and right subtrees.
# 3. Add 1 for the current root node.
# Time Complexity: O(n), where n = number of nodes.
# Space Complexity: O(h), where h = height of the tree (recursion stack).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepthOneLine(self, root): return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0

# LeetCode 538: Convert BST to Greater Tree
# Explanation:
# 1. Given a Binary Search Tree (BST), convert it so that each node's value
#    is replaced by the sum of all values greater than or equal to it.
# 2. Use reverse in-order traversal (right -> node -> left) to accumulate sum.

# Methods Used:
# - Reverse In-order Traversal (DFS)
# - Maintain running sum

# Time Complexity:
# - O(n), n = number of nodes

# Space Complexity:
# - O(h), recursion stack, h = height of tree


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # -------------------------------------------------------
    # Method 1: Reverse In-order Traversal
    # -------------------------------------------------------
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        self.total = 0

        def reverse_inorder(node):
            if not node:
                return
            reverse_inorder(node.right)
            self.total += node.val
            node.val = self.total
            reverse_inorder(node.left)

        reverse_inorder(root)
        return root



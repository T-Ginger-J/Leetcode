# LeetCode 450: Delete Node in a BST
# Explanation:
# Given a root of a BST and a key, delete the node with value == key and return the new root.
# BST property must remain valid.
#
# Method 1: Recursive Deletion (Optimal)
# - If node not found, return None
# - If node.val == key:
#     1. Node has no children → return None
#     2. Node has one child → return that child
#     3. Node has two children → find inorder successor (min in right subtree),
#        replace node's value with successor, and recursively delete successor
#
# Time Complexity: O(h), h = height of BST
# Space Complexity: O(h) recursion stack

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node found
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            # Node with two children: get inorder successor
            successor = root.right
            while successor.left:
                successor = successor.left
            root.val = successor.val
            root.right = self.deleteNode(root.right, successor.val)
        return root

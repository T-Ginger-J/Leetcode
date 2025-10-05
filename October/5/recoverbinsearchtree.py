# LeetCode 99: Recover Binary Search Tree
# Explanation:
# 1. Two nodes in a BST are swapped by mistake.
# 2. Use inorder traversal — values should be in ascending order.
# 3. When order breaks (prev.val > curr.val), mark those two nodes.
# 4. After traversal, swap their values to fix the BST.
# Time Complexity: O(n)
# Space Complexity: O(h) (recursion stack)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        self.first = self.second = self.prev = None
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node
            self.prev = node
            inorder(node.right)
        
        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val

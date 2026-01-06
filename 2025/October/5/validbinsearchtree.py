# LeetCode 98: Validate Binary Search Tree
# Explanation:
# 1. A valid BST satisfies: 
#    - Left subtree < root < Right subtree.
#    - Both subtrees must also be valid BSTs.
# 2. Use recursion with range limits (min_val, max_val) to validate each node.
# 3. Each node’s value must be strictly between the allowed range.
# Time Complexity: O(n), where n = number of nodes.
# Space Complexity: O(h), where h = tree height (recursion stack).

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        return validate(root)

    def isValidBSTOptimized(self, root: Optional[TreeNode]) -> bool:
        self.prev = float('-inf')
        def inorder(node):
            if not node:
                return True
            if not inorder(node.left): return False
            if node.val <= self.prev: return False
            self.prev = node.val
            return inorder(node.right)
        return inorder(root)
    
    # Example 1: Valid BST
root = TreeNode(2, TreeNode(1), TreeNode(3))
print(Solution().isValidBST(root))  # True

# Example 2: Invalid BST
root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
print(Solution().isValidBST(root))  # False

# Example 3: Single Node
root = TreeNode(1)
print(Solution().isValidBST(root))  # True
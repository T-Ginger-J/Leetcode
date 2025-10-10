# LeetCode 112: Path Sum
# Explanation:
# 1. Given a binary tree and a target sum, determine if there exists a root-to-leaf path 
#    such that the sum of node values equals the target.
# 2. Use DFS recursion:
#    - Subtract the current node value from the target.
#    - If we reach a leaf node and target == node.val, return True.
#    - Otherwise, recurse on left and right subtrees.
# Time Complexity: O(n) — visit each node once.
# Space Complexity: O(h) — recursion stack height, where h is the tree height.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and targetSum == root.val:
            return True
        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8, TreeNode(13), TreeNode(4, None, TreeNode(1)))
root.left.left = TreeNode(11, TreeNode(7), TreeNode(2))

print(Solution().hasPathSum(root, 22))  # True (5→4→11→2)
print(Solution().hasPathSum(root, 26))  # True (5→8→13)
print(Solution().hasPathSum(root, 5))   # False

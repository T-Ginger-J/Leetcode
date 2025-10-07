# LeetCode 105: Construct Binary Tree from Preorder and Inorder Traversal
# Explanation:
# 1. Preorder gives node order: [Root, Left, Right].
# 2. Inorder gives subtree structure: [Left, Root, Right].
# 3. The first element in preorder is always the root.
# 4. Find that root in inorder to divide into left and right subtrees.
# 5. Recurse on both sides using corresponding preorder slices.
# Time Complexity: O(n)
# Space Complexity: O(n) due to recursion and hashmap.

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        idx_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0
        
        def helper(left, right):
            if left > right:
                return None
            root_val = preorder[self.pre_idx]
            self.pre_idx += 1
            root = TreeNode(root_val)
            root.left = helper(left, idx_map[root_val] - 1)
            root.right = helper(idx_map[root_val] + 1, right)
            return root
        
        return helper(0, len(inorder) - 1)

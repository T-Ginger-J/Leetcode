# LeetCode 114: Flatten Binary Tree to Linked List
# Explanation:
# 1. Transform the binary tree into a "linked list" in-place following preorder traversal.
# 2. For each node:
#    - Recursively flatten left and right subtrees.
#    - Store the original right subtree.
#    - Move the flattened left subtree to the right, set left = None.
#    - Append the stored right subtree at the end of new right.
# Time Complexity: O(n) — every node visited once.
# Space Complexity: O(h) — recursion depth.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return
        
        self.flatten(root.left)
        self.flatten(root.right)

        temp = root.right
        root.right = root.left
        root.left = None
        
        curr = root
        while curr.right:
            curr = curr.right
        curr.right = temp

    def flattenOneLine(self, r, p=[None]):
        if not r: return
        self.flatten(r.right, p); self.flatten(r.left, p)
        r.right, r.left, p[0] = p[0], None, r

root = TreeNode(1)
root.left = TreeNode(2, TreeNode(3), TreeNode(4))
root.right = TreeNode(5, None, TreeNode(6))

Solution().flatten(root)

# Verify result:
curr = root
while curr:
    print(curr.val, end=" -> ")
    curr = curr.right
# Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6 ->
    
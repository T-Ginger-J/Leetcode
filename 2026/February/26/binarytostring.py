# LeetCode 606: Construct String from Binary Tree
# Explanation:
# 1. Given a binary tree, return a string representation with parentheses:
#    - Format: "node(left)(right)"
#    - Omit empty parentheses for null right child unless needed to preserve structure.
# 2. Approach:
#    - Use recursion (pre-order traversal).
#    - If node is None, return empty string.
#    - If node has a right child but no left, add empty parentheses for left.
#    - Concatenate strings accordingly.
# 3. Time Complexity: O(n), n = number of nodes
# 4. Space Complexity: O(h), recursion stack depth

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def tree2str(self, root: Optional[TreeNode]) -> str:

        if not root:
            return ""

        left_str = self.tree2str(root.left)
        right_str = self.tree2str(root.right)

        if right_str:
            return f"{root.val}({left_str})({right_str})"
        elif left_str:
            return f"{root.val}({left_str})"
        else:
            return f"{root.val}"


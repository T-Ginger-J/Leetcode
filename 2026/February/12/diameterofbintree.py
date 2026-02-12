# LeetCode 543: Diameter of Binary Tree
# Explanation:
# 1. The diameter is the length of the longest path between any two nodes.
# 2. Path length is measured in number of edges.
# 3. Use post-order traversal to compute height of left and right subtrees at each node,
#    and update maximum diameter as left_height + right_height.

# Methods Used:
# - Recursive DFS (post-order)
# - Track diameter during recursion

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
    # Method 1: DFS Post-order
    # -------------------------------------------------------
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        self.diameter = 0

        def height(node):
            if not node:
                return 0
            left = height(node.left)
            right = height(node.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)

        height(root)
        return self.diameter


# -------------------------------------------------------
# Examples (Including Edge Cases)
# -------------------------------------------------------

# Helper function: build tree easily
def build_tree(vals):
    if not vals:
        return None
    nodes = [TreeNode(v) if v is not None else None for v in vals]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

# Example 1
root1 = build_tree([1,2,3,4,5])
print(Solution().diameterOfBinaryTree(root1))  # 3 (path 4->2->1->3 or 5->2->1->3)

# Example 2 (Single node)
root2 = TreeNode(1)
print(Solution().diameterOfBinaryTree(root2))  # 0

# Example 3 (Left skewed)
root3 = build_tree([1,2,None,3,None,4])
print(Solution().diameterOfBinaryTree(root3))  # 3

# Example 4 (Right skewed)
root4 = build_tree([1,None,2,None,3,None,4])
print(Solution().diameterOfBinaryTree(root4))  # 3

# Example 5 (Balanced)
root5 = build_tree([1,2,3,4,5,6,7])
print(Solution().diameterOfBinaryTree(root5))  # 4 (path 4->2->1->3->7)

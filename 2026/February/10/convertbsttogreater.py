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


# -------------------------------------------------------
# Examples (Including Edge Cases)
# -------------------------------------------------------

# Helper function: In-order traversal
def inorder(node):
    if not node:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)

# Example 1
#      5
#     / \
#    2   13
root1 = TreeNode(5, TreeNode(2), TreeNode(13))
new_root1 = Solution().convertBST(root1)
print(inorder(new_root1))  # [20,18,13]

# Example 2 (Single node)
root2 = TreeNode(10)
new_root2 = Solution().convertBST(root2)
print(inorder(new_root2))  # [10]

# Example 3 (Left skewed)
root3 = TreeNode(3, TreeNode(2, TreeNode(1)))
new_root3 = Solution().convertBST(root3)
print(inorder(new_root3))  # [6,5,3]

# Example 4 (Right skewed)
root4 = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
new_root4 = Solution().convertBST(root4)
print(inorder(new_root4))  # [6,5,3]

# Example 5 (Empty tree)
root5 = None
new_root5 = Solution().convertBST(root5)
print(inorder(new_root5))  # []

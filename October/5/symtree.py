# LeetCode 101: Symmetric Tree
# Explanation:
# 1. A binary tree is symmetric if its left and right subtrees are mirror images.
# 2. Use recursion to compare corresponding nodes in mirrored positions.
# 3. Check that both values match and subtrees are mirrors of each other.
# Time Complexity: O(n), where n = number of nodes.
# Space Complexity: O(h), where h = tree height (recursion stack).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(t1, t2):
            if not t1 and not t2:
                return True
            if not t1 or not t2 or t1.val != t2.val:
                return False
            return isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)
        return isMirror(root.left, root.right) if root else True

# Example 1: Symmetric tree
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(3), TreeNode(4))
root.right = TreeNode(2, TreeNode(4), TreeNode(3))
print(Solution().isSymmetric(root))  # True

# Example 2: Asymmetric tree
root = TreeNode(1)
root.left = TreeNode(2, None, TreeNode(3))
root.right = TreeNode(2, None, TreeNode(3))
print(Solution().isSymmetric(root))  # False

# Example 3: Single node
root = TreeNode(1)
print(Solution().isSymmetric(root))  # True

# LeetCode 404: Sum of Left Leaves
# Explanation:
# 1. Traverse tree with DFS
# 2. If left child is leaf, add its value
# Time Complexity: O(n)
# Space Complexity: O(h)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        total = 0
        if root.left and not root.left.left and not root.left.right:
            total += root.left.val
        total += self.sumOfLeftLeaves(root.left)
        total += self.sumOfLeftLeaves(root.right)
        return total

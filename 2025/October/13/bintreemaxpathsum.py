# LeetCode 124: Binary Tree Maximum Path Sum
# Explanation:
# 1. The path can start and end at any node in the binary tree.
# 2. Use DFS to compute the max gain from each subtree.
# 3. At each node:
#    - Compute max left gain and right gain (ignore negative paths).
#    - Compute potential max path through this node = left + right + node.val.
#    - Update global max_sum if this path is higher.
# 4. Return max gain upward = node.val + max(left_gain, right_gain).
# Time Complexity: O(n)
# Space Complexity: O(h) where h is tree height (recursion stack).

class Solution:
    def maxPathSum(self, root):
        self.max_sum = float('-inf')

        def dfs(node):
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            self.max_sum = max(self.max_sum, node.val + left + right)
            return node.val + max(left, right)

        dfs(root)
        return self.max_sum
    
    def maxPathSumGlobal(self, root):
        res = [root.val]
        def dfs(node):
            if not node:
                return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            res[0] = max(res[0], node.val + left + right)
            return node.val + max(left, right)
        dfs(root)
        return res[0]


# Example 1
# Input: root = [1,2,3]
# Output: 6 (2 + 1 + 3)
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1, TreeNode(2), TreeNode(3))
print(Solution().maxPathSum(root))  # Output: 6

# Example 2
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42 (15 + 20 + 7)
root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(Solution().maxPathSum(root))  # Output: 42

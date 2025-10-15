# LeetCode 129: Sum Root to Leaf Numbers
# Explanation:
# 1. Each root-to-leaf path represents a number formed by concatenating node values.
# 2. Use DFS to traverse the tree, carrying the current number as you go.
# 3. When a leaf node is reached, add its number to the total sum.
# Time Complexity: O(n), where n = number of nodes.
# Space Complexity: O(h), where h = height of the tree (recursion stack).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, curr_sum):
            if not node:
                return 0
            curr_sum = curr_sum * 10 + node.val
            if not node.left and not node.right:
                return curr_sum
            return dfs(node.left, curr_sum) + dfs(node.right, curr_sum)
        return dfs(root, 0)


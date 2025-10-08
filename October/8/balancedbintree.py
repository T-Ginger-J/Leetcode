# LeetCode 110: Balanced Binary Tree
# Explanation:
# 1. A binary tree is balanced if for every node, the height difference between left and right ≤ 1.
# 2. Use DFS recursion: compute height of left and right subtrees.
# 3. If any subtree is unbalanced, propagate -1 upwards to indicate imbalance.
# 4. If balanced, return the actual height.
# Time Complexity: O(n) — each node is visited once.
# Space Complexity: O(h) — recursion stack height, where h is the tree height.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            left = dfs(node.left)
            if left == -1:
                return -1
            right = dfs(node.right)
            if right == -1 or abs(left - right) > 1:
                return -1
            return max(left, right) + 1

        return dfs(root) != -1

    def isBalancedOnePass(self, root):
        def check(node):
            if not node:
                return True, 0
            left_bal, left_height = check(node.left)
            right_bal, right_height = check(node.right)
            balanced = left_bal and right_bal and abs(left_height - right_height) <= 1
            return balanced, max(left_height, right_height) + 1
        return check(root)[0]
    
    def isBalancedOneLine(self, r):
        f = lambda n: (h:=0) if not n else (max(f(n.left), f(n.right)) + 1 if abs(f(n.left)-f(n.right))<=1 else -1)
        return f(r) != -1
    
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))
print(Solution().isBalanced(root))  # True

root.right.right = TreeNode(8, TreeNode(9, TreeNode(10)))
print(Solution().isBalanced(root))  # False

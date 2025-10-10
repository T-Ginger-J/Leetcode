# LeetCode 113: Path Sum II
# Explanation:
# 1. Find all root-to-leaf paths where each path's sum equals targetSum.
# 2. Use DFS recursion to traverse the tree.
# 3. Keep a running list `path` to track current nodes and a `res` list for valid paths.
# 4. When a leaf node’s path sum equals targetSum, append a copy of the path to results.
# Time Complexity: O(n) — every node is visited once.
# Space Complexity: O(h) — recursion stack, where h is the height of the tree.

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        def dfs(node, curr_sum, path):
            if not node:
                return
            path.append(node.val)
            curr_sum += node.val
            if not node.left and not node.right and curr_sum == targetSum:
                res.append(path[:])
            dfs(node.left, curr_sum, path)
            dfs(node.right, curr_sum, path)
            path.pop()
        dfs(root, 0, [])
        return res

    def pathSumStack(self, root, targetSum):
        if not root:
            return []
        res, stack = [], [(root, [root.val], targetSum - root.val)]
        while stack:
            node, path, remain = stack.pop()
            if not node.left and not node.right and remain == 0:
                res.append(path)
            if node.right:
                stack.append((node.right, path + [node.right.val], remain - node.right.val))
            if node.left:
                stack.append((node.left, path + [node.left.val], remain - node.left.val))
        return res

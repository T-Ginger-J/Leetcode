# LeetCode 563: Binary Tree Tilt
# Explanation:
# 1. Given a binary tree, the tilt of a tree node is the absolute difference between the sum of all left subtree node values and the sum of all right subtree node values.
# 2. Approach:
#    - Use DFS to compute the sum of subtree for each node.
#    - Accumulate the tilt (abs(left_sum - right_sum)) at each node.
# 3. Time Complexity: O(n), n = number of nodes
# 4. Space Complexity: O(h), h = height of tree (recursive stack)

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # -------------------------------------------------------
    # Method 1: DFS post-order
    # -------------------------------------------------------
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total_tilt = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            self.total_tilt += abs(left_sum - right_sum)
            return node.val + left_sum + right_sum

        dfs(root)
        return self.total_tilt

    # -------------------------------------------------------
    # Method 2: Iterative post-order using stack
    # -------------------------------------------------------
    def findTiltIterative(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        total_tilt = 0
        stack = [(root, False)]
        sums = {}

        while stack:
            node, visited = stack.pop()
            if node is None:
                continue
            if visited:
                left_sum = sums.get(node.left, 0)
                right_sum = sums.get(node.right, 0)
                total_tilt += abs(left_sum - right_sum)
                sums[node] = node.val + left_sum + right_sum
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        return total_tilt



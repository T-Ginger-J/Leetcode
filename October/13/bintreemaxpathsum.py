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

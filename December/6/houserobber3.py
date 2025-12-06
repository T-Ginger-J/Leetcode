# LeetCode 337: House Robber III
# Explanation:
# 1. Use DFS that returns two values: (rob, not_rob)
# 2. rob = node.val + left.not_rob + right.not_rob
# 3. not_rob = max(left) + max(right)
# 4. Final result = max(root.rob, root.not_rob)
# Time Complexity: O(n)
# Space Complexity: O(h)

class Solution:
    def rob(self, root):
        def dfs(node):
            if not node:
                return (0, 0)  # (rob, not_rob)

            left = dfs(node.left)
            right = dfs(node.right)

            rob = node.val + left[1] + right[1]
            not_rob = max(left) + max(right)

            return (rob, not_rob)

        return max(dfs(root))


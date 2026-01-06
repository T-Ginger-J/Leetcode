# LeetCode 236: Lowest Common Ancestor of a Binary Tree
# Explanation:
# Use DFS:
# - If current node is p or q, return it.
# - Recurse left and right.
# - If both sides return non-null → this node is the LCA.
# - Otherwise propagate whichever side is non-null.
#
# Time Complexity: O(n)
# Space Complexity: O(h) recursion depth (worst O(n))

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left if left else right

# Example usage:
# sol = Solution()
# print(sol.lowestCommonAncestor(root, p, q).val)
# print(sol.lowestCommonAncestor(root, a, c).val)

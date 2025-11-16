# LeetCode 235: Lowest Common Ancestor of a BST
# Explanation:
# Because it's a BST:
# - If both p and q are greater than root → go right
# - If both p and q are smaller than root → go left
# - Otherwise, root is the LCA
#
# Time Complexity: O(log n) on balanced BST, O(n) worst case
# Space Complexity: O(1)

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root
        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur
            
    def lowestCommonAncestorRecursive(self, root, p, q):
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        return root


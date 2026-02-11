class Solution:

    # -------------------------------------------------------
    # Method 1: Reverse In-order Traversal
    # -------------------------------------------------------
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        self.total = 0

        def reverse_inorder(node):
            if not node:
                return
            reverse_inorder(node.right)
            self.total += node.val
            node.val = self.total
            reverse_inorder(node.left)

        reverse_inorder(root)
        return root



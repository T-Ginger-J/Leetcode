# LeetCode 94: Binary Tree Inorder Traversal
# Explanation:
# 1. Inorder traversal visits nodes in order: Left → Node → Right.
# 2. Use recursion to traverse left, append current node, then traverse right.
# 3. Alternatively, use a stack to simulate recursion iteratively.
# Time Complexity: O(n), where n = number of nodes.
# Space Complexity: O(n) in worst case (recursion stack or explicit stack).

class Solution:
    def inorderTraversal(self, root: TreeNode):
        res = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            res.append(node.val)
            dfs(node.right)
        dfs(root)
        return res

    def inorderTraversalStack(self, root: TreeNode):
        res, stack = [], []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right
        return res
    
    def inorderTraversalOneLine(self, root: TreeNode):
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []


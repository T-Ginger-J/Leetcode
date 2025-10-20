# LeetCode 145: Binary Tree Postorder Traversal
# Explanation:
# 1. Postorder traversal visits nodes in order: Left → Right → Root.
# 2. Use recursion to traverse both subtrees before visiting the current node.
# Time Complexity: O(n)
# Space Complexity: O(n) (recursive stack)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> list[int]:
        res = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            res.append(node.val)
        dfs(root)
        return res

# Example 1
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
print(Solution().postorderTraversal(root))
# Output: [3, 2, 1]

# Example 2
root = TreeNode(1, TreeNode(2), TreeNode(3))
print(Solution().postorderTraversal(root))
# Output: [2, 3, 1]

# Example 3
print(Solution().postorderTraversal(None))
# Output: []

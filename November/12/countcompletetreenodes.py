# LeetCode 222: Count Complete Tree Nodes
# Explanation:
# 1. Compute left and right subtree heights.
# 2. If equal, left subtree is full: count = 2^left_height - 1 + recurse on right.
# 3. If not equal, right subtree is full: count = 2^right_height - 1 + recurse on left.
# Time Complexity: O(log^2 n)
# Space Complexity: O(log n)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def height(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h

        if not root:
            return 0

        left_height = height(root.left)
        right_height = height(root.right)

        if left_height == right_height:
            return (1 << left_height) + self.countNodes(root.right)
        else:
            return (1 << right_height) + self.countNodes(root.left)
# Construct example tree: [1,2,3,4,5,6]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

sol = Solution()
print(sol.countNodes(root))  # 6
print(sol.countNodes(TreeNode(1)))  # 1
print(sol.countNodes(None))  # 0

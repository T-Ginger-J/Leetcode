# LeetCode 230: Kth Smallest Element in a BST
# Explanation:
# 1. A BST's inorder traversal produces values in sorted order.
# 2. Perform an inorder traversal until we reach the k-th element.
#
# Time Complexity: O(h + k) where h = tree height
# Space Complexity: O(h) for recursion stack

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        stack = []
        curr = root

        while True:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val

            curr = curr.right

    def kthSmallestRecursive(self, root: TreeNode, k: int) -> int:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        gen = inorder(root)
        for _ in range(k - 1):
            next(gen)
        return next(gen)



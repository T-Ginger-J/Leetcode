# LeetCode 226: Invert Binary Tree
# Explanation:
# 1. Recursively swap left and right children.
# 2. Base case: if node is None, return None.
# Time Complexity: O(n) — visits each node once.
# Space Complexity: O(h) — recursion stack height (worst O(n)).

class Solution:
    def invertTree(self, root):
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

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

# Input: [4,2,7,1,3,6,9]
# Output after invert: [4,7,2,9,6,3,1]
from collections import deque

def levelOrder(root):
    res, q = [], deque([root])
    while q:
        node = q.popleft()
        if node:
            res.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            res.append(None)
    return res

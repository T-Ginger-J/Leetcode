# LeetCode 100: Same Tree
# Explanation:
# 1. Two binary trees are the same if:
#    - Their roots have the same value, and
#    - Their left and right subtrees are also the same.
# 2. Use recursion to compare nodes at the same position.
# Time Complexity: O(n), where n = number of nodes.
# Space Complexity: O(h), where h = tree height (recursion stack).

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    def isSameTreeIterative(self, p: TreeNode, q: TreeNode) -> bool:
        queue = deque([(p, q)])
        while queue:
            n1, n2 = queue.popleft()
            if not n1 and not n2:
                continue
            if not n1 or not n2 or n1.val != n2.val:
                return False
            queue.append((n1.left, n2.left))
            queue.append((n1.right, n2.right))
        return True

    isSameTreeOneLine = lambda self,p,q: not p and not q or (p and q and p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))


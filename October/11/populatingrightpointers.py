# LeetCode 116: Populating Next Right Pointers in Each Node
# Explanation:
# 1. We are given a perfect binary tree (all leaves on the same level).
# 2. The goal is to connect each node’s `next` pointer to its right neighbor.
# 3. Use level traversal with existing next pointers (no extra space).
# 4. For each node:
#    - Connect left child to right child.
#    - Connect right child to the next node’s left child if it exists.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left
        return root

    def connectOneLine(self, r):
        if r and r.left: r.left.next, r.right.next = r.right, r.next and r.next.left and self.connect(r.left) or self.connect(r.right)
        return r

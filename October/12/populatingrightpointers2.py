# LeetCode 117: Populating Next Right Pointers in Each Node II
# Explanation:
# 1. Similar to LeetCode 116 but works for ANY binary tree (not necessarily perfect).
# 2. For each level:
#    - Use a dummy node to track the start of the next level.
#    - Connect children of current level nodes in sequence.
# 3. Move down level by level using established next pointers.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        curr = root
        while curr:
            dummy = Node(0)
            tail = dummy
            while curr:
                if curr.left:
                    tail.next = curr.left
                    tail = tail.next
                if curr.right:
                    tail.next = curr.right
                    tail = tail.next
                curr = curr.next
            curr = dummy.next
        return root

# LeetCode 109: Convert Sorted List to Binary Search Tree
# Explanation:
# 1. Convert a sorted linked list to a height-balanced BST.
# 2. Use slow/fast pointers to find the middle node — this becomes the root.
# 3. Recursively construct left subtree from the left half, and right subtree from the right half.
# 4. This ensures the BST is balanced.
# Time Complexity: O(n log n) — each level requires scanning the list.
# Space Complexity: O(log n) — recursion depth.

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)

        # Find middle node
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None  # Split list

        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root

# LeetCode 143: Reorder List
# Explanation:
# 1. Use slow/fast pointers to find the middle of the list.
# 2. Reverse the second half of the list.
# 3. Merge the two halves by alternating nodes.
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # Step 1: Find middle (slow/fast pointers)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        # Step 3: Merge two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2


# Helper to build and print list
def printList(node):
    vals = []
    while node:
        vals.append(node.val)
        node = node.next
    print(vals)

# Build list: [1, 2, 3, 4]
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
Solution().reorderList(head)
printList(head)  # ✅ Output: [1, 4, 2, 3]

# Build list: [1, 2, 3, 4, 5]
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
Solution().reorderList(head)
printList(head)  # ✅ Output: [1, 5, 2, 4, 3]

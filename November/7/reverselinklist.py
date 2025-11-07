# LeetCode 206: Reverse Linked List
# Explanation:
# 1. Use three pointers: prev, curr, next.
# 2. Reverse links one by one while traversing the list.
# 3. Return prev as new head.
# Time Complexity: O(n)
# Space Complexity: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

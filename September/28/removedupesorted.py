# LeetCode 83: Remove Duplicates from Sorted List
# Explanation:
# 1. Iterate through list with pointer.
# 2. If current node has same value as next, skip next node.
# 3. Otherwise move pointer forward.
# Time Complexity: O(n)
# Space Complexity: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head
        while node:
            while node.next and node.val == node.next.val:
                node.next = node.next.next
            node = node.next
        return head

    deleteDuplicatesOneLine=lambda s,h:h and (h.next:=s.deleteDuplicates(h.next)) or h

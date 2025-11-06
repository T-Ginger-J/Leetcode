# LeetCode 203: Remove Linked List Elements
# Explanation:
# 1. Use a dummy node to simplify head deletion.
# 2. Traverse list and skip nodes where node.val == val.
# 3. Return dummy.next as new head.
# Time Complexity: O(n)
# Space Complexity: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0, head)
        current = dummy
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next

    def removeElementsRecusive(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head
    
    def removeElementsOneLine(self, h, v): return h and (self.removeElements(h.next,v) if h.val==v else ListNode(h.val,self.removeElements(h.next,v)))

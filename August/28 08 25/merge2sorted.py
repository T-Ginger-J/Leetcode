
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# O(n)
class Solution:
    def mergeTwoListsIterative(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        
        # attach remaining nodes
        current.next = l1 or l2
        
        return dummy.next
    
    def mergeTwoListsRecursive(self, l1, l2):
        return l1 if not l2 else l2 if not l1 else (l1 if l1.val < l2.val else l2).__setattr__('next', self.mergeTwoLists(l1.next if l1.val < l2.val else l1, l2 if l1.val < l2.val else l2.next)) or (l1 if l1.val < l2.val else l2)


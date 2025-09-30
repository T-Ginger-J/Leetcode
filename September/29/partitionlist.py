# LeetCode 86: Partition List
# Explanation:
# 1. Maintain two lists: one for nodes < x, one for nodes >= x.
# 2. Traverse and append nodes to appropriate list.
# 3. Merge the two lists at the end.
# Time Complexity: O(n)
# Space Complexity: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)
        
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next
        
        after.next = None
        before.next = after_head.next
        return before_head.next
    
    def partitionOptimized(self, head: ListNode, x: int) -> ListNode:
        small, large = ListNode(0), ListNode(0)
        s, l = small, large
        while head:
            if head.val < x:
                s.next, s = head, head
            else:
                l.next, l = head, head
            head = head.next
        l.next = None
        s.next = large.next
        return small.next
    
    partitionOneLine=lambda s,h,x:(lambda a,b:(a.next:=b.next,a.next))(ListNode(0),ListNode(0))or[(lambda p,q:(p.next,q.next))(a:=ListNode(0),b:=ListNode(0))or[None]][-1]

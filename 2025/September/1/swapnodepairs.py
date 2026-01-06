# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # Count the total number of nodes
        def count_nodes(node):
            cnt = 0
            while node:
                cnt += 1
                node = node.next
            return cnt

        total = count_nodes(head)
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while total >= k:
            curr = prev.next
            nxt = curr.next
            # Reverse k nodes
            for _ in range(1, k):
                curr.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = curr.next
            prev = curr
            total -= k

        return dummy.next

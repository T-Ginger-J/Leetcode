class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Step 1: Move prev to node before 'left'
        for _ in range(left - 1):
            prev = prev.next

        # Step 2: Reverse sublist from left to right
        curr = prev.next
        nxt = None
        for _ in range(right - left):
            nxt = curr.next
            curr.next = nxt.next
            nxt.next = prev.next
            prev.next = nxt

        return dummy.next

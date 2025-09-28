class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head
        while node:
            while node.next and node.val == node.next.val:
                node.next = node.next.next
            node = node.next
        return head

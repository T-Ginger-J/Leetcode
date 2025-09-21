# O(n)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)  # dummy node to handle edge cases
        slow = fast = dummy

        # move fast n+1 steps ahead so slow ends up before the target
        for _ in range(n + 1):
            fast = fast.next

        # move both until fast reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # delete the nth node
        slow.next = slow.next.next

        return dummy.next

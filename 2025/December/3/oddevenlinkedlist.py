# LeetCode 328: Odd Even Linked List
# Explanation:
# - We split the linked list into two lists:
#     * odd nodes (1st, 3rd, 5th, ...)
#     * even nodes (2nd, 4th, 6th, ...)
# - Connect the tail of the odd list to the head of the even list.
# - Preserve the original relative order inside both odd and even lists.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        odd = head
        even = head.next
        even_head = even

        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head
        return head

# Utility to build a list for testing
def build(lst):
    from typing import Optional
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next
    dummy = ListNode()
    curr = dummy
    for x in lst:
        curr.next = ListNode(x)
        curr = curr.next
    return dummy.next

# Utility to print list
def dump(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

head = build([1,2,3,4,5])
print(dump(Solution().oddEvenList(head)))  # [1,3,5,2,4]

head = build([2,1,3,5,6,4,7])
print(dump(Solution().oddEvenList(head)))  # [2,3,6,7,1,5,4]

head = build([1])
print(dump(Solution().oddEvenList(head)))  # [1]

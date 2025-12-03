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

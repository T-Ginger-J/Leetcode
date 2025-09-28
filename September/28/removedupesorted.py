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


# Example usage:
# def list_to_linked(lst):
#     dummy = ListNode(0)
#     curr = dummy
#     for v in lst:
#         curr.next = ListNode(v)
#         curr = curr.next
#     return dummy.next
#
# def linked_to_list(node):
#     res = []
#     while node:
#         res.append(node.val)
#         node = node.next
#     return res
#
# sol = Solution()
# head = list_to_linked([1,1,2])
# print(linked_to_list(sol.deleteDuplicates(head)))  # [1,2]
# head = list_to_linked([1,1,2,3,3])
# print(linked_to_list(sol.deleteDuplicates(head)))  # [1,2,3]

# LeetCode 82: Remove Duplicates from Sorted List II
# Explanation:
# 1. Use dummy node to handle edge cases (duplicates at head).
# 2. Iterate with prev and current pointers.
# 3. Skip nodes while duplicates exist.
# 4. Attach prev.next to next distinct node.
# Time Complexity: O(n)
# Space Complexity: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        prev = dummy
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next
            head = head.nex
        return dummy.next
    
    deleteDuplicatesOneLine=lambda s,h:None if not h else h if not h.next or h.val!=h.next.val else s.deleteDuplicates(next((n for n in iter(lambda:h: (h:=h.next) and h, None),None)))

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
# head = list_to_linked([1,2,3,3,4,4,5])
# print(linked_to_list(sol.deleteDuplicates(head)))  # [1,2,5]
# head = list_to_linked([1,1,1,2,3])
# print(linked_to_list(sol.deleteDuplicates(head)))  # [2,3]

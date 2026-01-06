# LeetCode 206: Reverse Linked List
# Explanation:
# 1. Use three pointers: prev, curr, next.
# 2. Reverse links one by one while traversing the list.
# 3. Return prev as new head.
# Time Complexity: O(n)
# Space Complexity: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    
    def reverseListRecursive(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p

class Solution:
    def reverseListOneLine(self, h, p=None): return self.reverseList(h.next,h) if h else p


def build_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for n in arr:
        curr.next = ListNode(n)
        curr = curr.next
    return dummy.next

def print_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

sol = Solution()
head = build_list([1,2,3,4,5])
print(print_list(sol.reverseList(head)))  # [5,4,3,2,1]


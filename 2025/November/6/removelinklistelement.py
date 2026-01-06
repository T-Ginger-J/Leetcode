# LeetCode 203: Remove Linked List Elements
# Explanation:
# 1. Use a dummy node to simplify head deletion.
# 2. Traverse list and skip nodes where node.val == val.
# 3. Return dummy.next as new head.
# Time Complexity: O(n)
# Space Complexity: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode(0, head)
        current = dummy
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next

    def removeElementsRecusive(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head
    
    def removeElementsOneLine(self, h, v): return h and (self.removeElements(h.next,v) if h.val==v else ListNode(h.val,self.removeElements(h.next,v)))

# Helper to build and print linked lists
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
head = build_list([1,2,6,3,4,5,6])
print(print_list(sol.removeElements(head, 6)))  # [1, 2, 3, 4, 5]

# LeetCode 92: Reverse Linked List II
# Explanation:
# 1. We need to reverse a linked list between positions left and right (1-indexed).
# 2. Use a dummy node to simplify edge cases (reversing from head).
# 3. Traverse to node before 'left', then reverse sublist until 'right'.
# 4. Reconnect reversed sublist back to main list.
# Time Complexity: O(n)
# Space Complexity: O(1)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

# Helper functions
def build_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for v in arr:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def to_array(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

# Example 1
head = build_list([1,2,3,4,5])
res = Solution().reverseBetween(head, 2, 4)
print(to_array(res))  # [1,4,3,2,5]

# Example 2
head = build_list([5])
res = Solution().reverseBetween(head, 1, 1)
print(to_array(res))  # [5]

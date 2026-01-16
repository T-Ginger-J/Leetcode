# LeetCode 445: Add Two Numbers II
# Explanation:
# Given two non-empty linked lists representing two non-negative integers,
# digits are stored in **forward order** (most significant digit first).
# Return a linked list representing their sum, also in forward order.
#
# Method 1: Stack-Based (Optimal)
# - Push all digits of both lists onto stacks.
# - Pop from stacks to add digits from least significant to most significant.
# - Handle carry and build the result list from head.
#
# Time Complexity: O(max(m, n)), where m and n are lengths of the lists
# Space Complexity: O(m + n) (for stacks)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        head = None
        while stack1 or stack2 or carry:
            x = stack1.pop() if stack1 else 0
            y = stack2.pop() if stack2 else 0
            total = x + y + carry
            carry = total // 10
            node = ListNode(total % 10)
            node.next = head
            head = node
        return head


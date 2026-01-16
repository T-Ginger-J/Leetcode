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

# Helper function to print linked list
def print_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    print(res)

# Additional Examples (Edge Cases and Non-LeetCode Examples)

sol = Solution()

# Example 1: Same length
l1 = ListNode(7, ListNode(2, ListNode(4, ListNode(3))))
l2 = ListNode(5, ListNode(6, ListNode(4)))
res1 = sol.addTwoNumbers(l1, l2)
print_list(res1)
# Expected output: [7, 8, 0, 7]  (7243 + 564 = 7807)

# Example 2: Different lengths, with carry
l3 = ListNode(9, ListNode(9))
l4 = ListNode(1)
res2 = sol.addTwoNumbers(l3, l4)
print_list(res2)
# Expected output: [1, 0, 0]  (99 + 1 = 100)

# Example 3: Single node lists
l5 = ListNode(0)
l6 = ListNode(0)
res3 = sol.addTwoNumbers(l5, l6)
print_list(res3)
# Expected output: [0]

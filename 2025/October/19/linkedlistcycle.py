# LeetCode 141: Linked List Cycle
# Explanation:
# 1. Use two pointers: slow and fast.
# 2. Move slow by one step, fast by two steps.
# 3. If fast and slow meet, there is a cycle.
# 4. If fast reaches None, no cycle exists.
# Time Complexity: O(n)
# Space Complexity: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
    
    def hasCycleHash(self, head: ListNode) -> bool:
        visited = set()
        while head:
            if head in visited:
                return True
            visited.add(head)
            head = head.next
        return False

# Example 1: Cycle exists
node1, node2, node3, node4 = ListNode(3), ListNode(2), ListNode(0), ListNode(-4)
node1.next, node2.next, node3.next, node4.next = node2, node3, node4, node2
print(Solution().hasCycle(node1))
# Output: True

# Example 2: No cycle
a, b = ListNode(1), ListNode(2)
a.next = b
print(Solution().hasCycle(a))
# Output: False

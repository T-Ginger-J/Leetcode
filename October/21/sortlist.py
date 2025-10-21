# LeetCode 148: Sort List (Optimized Iterative Merge Sort)
# Explanation:
# 1. Avoid recursion to reduce call stack usage.
# 2. Bottom-up approach merges sublists of increasing size (1, 2, 4, 8...).
# 3. Improves memory usage while maintaining O(n log n) time.
# Time Complexity: O(n log n)
# Space Complexity: O(1)

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        # Get length
        length, node = 0, head
        while node:
            length += 1
            node = node.next

        dummy = ListNode(0, head)
        size = 1
        while size < length:
            tail, curr = dummy, dummy.next
            while curr:
                left = curr
                right = self.split(left, size)
                curr = self.split(right, size)
                tail = self.merge(left, right, tail)
            size *= 2
        return dummy.next

    def split(self, head, size):
        for i in range(size - 1):
            if head and head.next:
                head = head.next
            else:
                break
        rest = head.next if head else None
        if head:
            head.next = None
        return rest

    def merge(self, l1, l2, head):
        curr = head
        while l1 and l2:
            if l1.val < l2.val:
                curr.next, l1 = l1, l1.next
            else:
                curr.next, l2 = l2, l2.next
            curr = curr.next
        curr.next = l1 or l2
        while curr.next:
            curr = curr.next
        return curr


# LeetCode 147: Insertion Sort List
# Explanation:
# 1. Iterate through the linked list, inserting each node into its correct position in a sorted portion.
# 2. Use a dummy head to simplify insertion logic.
# 3. Compare current node’s value with sorted nodes, and insert before the first larger node.
# Time Complexity: O(n²)
# Space Complexity: O(1)

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = head
        while curr:
            prev = dummy
            while prev.next and prev.next.val < curr.val:
                prev = prev.next
            nxt = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = nxt
        return dummy.next

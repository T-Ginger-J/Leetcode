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

    def insertionSortListTail(self, head: ListNode) -> ListNode:
        if not head:
            return head
        dummy = ListNode(0, head)
        last_sorted = head
        curr = head.next
        while curr:
            if last_sorted.val <= curr.val:
                last_sorted = last_sorted.next
            else:
                prev = dummy
                while prev.next.val <= curr.val:
                    prev = prev.next
                last_sorted.next = curr.next
                curr.next = prev.next
                prev.next = curr
            curr = last_sorted.next
        return dummy.next

# Helper functions
def create_list(arr):
    dummy = ListNode(0)
    curr = dummy
    for val in arr:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    print(res)

# Example 1
head = create_list([4,2,1,3])
print_list(Solution().insertionSortList(head))
# Output: [1,2,3,4]

# Example 2
head = create_list([-1,5,3,4,0])
print_list(Solution().insertionSortList(head))
# Output: [-1,0,3,4,5]


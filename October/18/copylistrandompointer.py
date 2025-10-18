# LeetCode 138: Copy List with Random Pointer
# Explanation:
# 1. Each node has `next` and `random` pointers.
# 2. Step 1: Insert copied node next to each original node (interleaving).
# 3. Step 2: Assign random pointers of copied nodes using original's random links.
# 4. Step 3: Separate original and copied nodes into two lists.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = x
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Insert cloned nodes
        curr = head
        while curr:
            new_node = Node(curr.val, curr.next)
            curr.next = new_node
            curr = new_node.next

        # Step 2: Assign random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Step 3: Separate the cloned list
        curr, copy = head, head.next
        clone_head = copy
        while curr:
            curr.next = curr.next.next
            copy.next = copy.next.next if copy.next else None
            curr = curr.next
            copy = copy.next

        return clone_head

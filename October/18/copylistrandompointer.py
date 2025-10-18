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

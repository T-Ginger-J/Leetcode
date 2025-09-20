class Solution:
    def rotateRight(self, head, k: int):
        if not head or not head.next or k == 0:
            return head
        
        # Find length
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        k %= length
        if k == 0:
            return head
        
        # Make it circular
        tail.next = head
        
        # Find new tail
        steps_to_new_tail = length - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head

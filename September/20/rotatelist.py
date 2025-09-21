# LeetCode 61: Rotate List
# Explanation:
# 1. Find the length of the list.
# 2. Connect the tail to the head to make it circular.
# 3. Move (length - k % length - 1) steps from head to find the new tail.
# 4. Break the circle and set new head as tail.next.
# Time Complexity: O(n)
# Space Complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

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
    
    def rotateRightTwoPass(self, head, k: int):
        if not head or not head.next:
            return head
        # count length
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1
        k %= n
        if k == 0:
            return head
        # find new head
        cur = head
        for _ in range(n - k - 1):
            cur = cur.next
        new_head = cur.next
        cur.next = None
        tail.next = head
        return new_head
    
    rotateRightOneLine=lambda s,h,k:(lambda n:(lambda t:(t.next,h:=[h])[0])((lambda x:[x.append(x.pop(0)) for _ in range(k%n)],x:=[])[1]))(sum(bool(h:=h.next)or x.append(h) for x in [[]]))(h)


# Example usage:
# # Input: 1->2->3->4->5, k=2
# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# sol = Solution()
# new_head = sol.rotateRight(head, 2)
# while new_head:
#     print(new_head.val, end=' ')
#     new_head = new_head.next
# # Output: 4 5 1 2 3

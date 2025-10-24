# LeetCode 160: Intersection of Two Linked Lists
# Explanation:
# 1. Use two pointers `a` and `b` starting at headA and headB.
# 2. When either pointer reaches the end, redirect it to the other list’s head.
# 3. If the lists intersect, pointers will meet at the intersection node.
# 4. If not, both will reach None at the same time.
# Time Complexity: O(m + n)
# Space Complexity: O(1)

class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        a, b = headA, headB
        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a

# Example setup:
# A: 4 -> 1 \
#              8 -> 4 -> 5
# B:    5 -> 0 -> 1 /
#
# Intersection at node with value 8

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Build example lists
intersect = ListNode(8, ListNode(4, ListNode(5)))
headA = ListNode(4, ListNode(1, intersect))
headB = ListNode(5, ListNode(0, ListNode(1, intersect)))

print(Solution().getIntersectionNode(headA, headB).val)  # Output: 8

# LeetCode 237: Delete Node in a Linked List
# Explanation:
# You cannot access the head or previous node.
# So instead:
# - Copy the value of the next node into the current node.
# - Skip the next node by pointing current.next to next.next
#
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


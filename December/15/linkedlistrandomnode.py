# LeetCode 382: Linked List Random Node
# Explanation:
# 1. Iterate through the list, update result with probability 1/i
# Time Complexity: O(n) per getRandom call
# Space Complexity: O(1)

import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        result, node, i = 0, self.head, 1
        while node:
            if random.randint(1, i) == 1:
                result = node.val
            node = node.next
            i += 1
        return result

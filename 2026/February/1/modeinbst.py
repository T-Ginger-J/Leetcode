# LeetCode 501: Find Mode in Binary Search Tree
# Explanation:
# Given the root of a Binary Search Tree (BST), return all the mode(s)
# (the most frequently occurring element(s)).
#
# Key BST Property:
# - In-order traversal of BST yields values in non-decreasing order.
#
# Method 1: In-order Traversal with Frequency Tracking (Optimal)
# - Track current value count, max frequency, and result list.
# - Update modes when a new max frequency is found.
#
# Time Complexity: O(n)
# Space Complexity: O(h) for recursion stack (h = tree height)

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.prev = None
        self.count = 0
        self.max_count = 0
        self.res = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)

            if self.prev == node.val:
                self.count += 1
            else:
                self.count = 1
            if self.count > self.max_count:
                self.max_count = self.count
                self.res = [node.val]
            elif self.count == self.max_count:
                self.res.append(node.val)
            self.prev = node.val

            inorder(node.right)

        inorder(root)
        return self.res


# Alternate Python Solution: Two-Pass In-order Traversal
# - First pass computes max frequency
# - Second pass collects values with that frequency

class SolutionTwoPass:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        prev = None
        count = max_count = 0

        def inorder1(node):
            nonlocal prev, count, max_count
            if not node:
                return
            inorder1(node.left)
            if prev == node.val:
                count += 1
            else:
                count = 1
            max_count = max(max_count, count)
            prev = node.val
            inorder1(node.right)

        def inorder2(node):
            nonlocal prev, count
            if not node:
                return
            inorder2(node.left)
            if prev == node.val:
                count += 1
            else:
                count = 1
            if count == max_count:
                res.append(node.val)
            prev = node.val
            inorder2(node.right)

        inorder1(root)
        prev = None
        count = 0
        res = []
        inorder2(root)
        return res

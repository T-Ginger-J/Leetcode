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


# Additional Examples (Edge Cases and Non-LeetCode Examples)

# Helper to build tree
def build_tree(vals):
    if not vals:
        return None
    nodes = [None if v is None else TreeNode(v) for v in vals]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

sol = Solution()

# Example 1: Single node
root1 = build_tree([1])
print(sol.findMode(root1))
# Expected output: [1]

# Example 2: Multiple modes
root2 = build_tree([1,None,2,2])
print(sol.findMode(root2))
# Expected output: [2]

# Example 3: All values same
root3 = build_tree([2,2,2])
print(sol.findMode(root3))
# Expected output: [2]

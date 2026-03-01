# LeetCode 617: Merge Two Binary Trees
# Explanation:
# 1. Given two binary trees root1 and root2.
# 2. If both nodes exist, their values are summed.
# 3. If only one node exists, use that node.
# 4. If both are None, result is None.
# 5. Recursively merge left and right subtrees.
#
# Method 1 (Recursive DFS):
# - If one node is None, return the other.
# - Otherwise, create new node with summed value.
# - Recursively merge children.
#
# Time Complexity: O(N)
#   N = total number of nodes in both trees.
# Space Complexity: O(H)
#   H = height of tree (recursion stack).
#
# Alternative Method 1 (Iterative BFS):
# - Use a queue to traverse both trees simultaneously.
# - Modify first tree in place.
#
# Alternative Method 2 (In-Place Recursive):
# - Reuse nodes of root1 to save memory.
# - No new tree allocation.


from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # Main Solution: Recursive DFS (Creates New Tree)
    def mergeTrees(self, root1: Optional[TreeNode],
                   root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root1 and not root2:
            return None

        if not root1:
            return root2

        if not root2:
            return root1

        node = TreeNode(root1.val + root2.val)

        node.left = self.mergeTrees(root1.left, root2.left)
        node.right = self.mergeTrees(root1.right, root2.right)

        return node


    # Alternative Solution 1: Iterative BFS (In-Place on root1)
    def mergeTreesAlt1(self, root1: Optional[TreeNode],
                       root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root1:
            return root2

        if not root2:
            return root1

        queue = deque([(root1, root2)])

        while queue:
            n1, n2 = queue.popleft()

            n1.val += n2.val

            if n1.left and n2.left:
                queue.append((n1.left, n2.left))
            elif not n1.left:
                n1.left = n2.left

            if n1.right and n2.right:
                queue.append((n1.right, n2.right))
            elif not n1.right:
                n1.right = n2.right

        return root1


    # Alternative Solution 2: Recursive In-Place Merge
    def mergeTreesAlt2(self, root1: Optional[TreeNode],
                       root2: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root1:
            return root2

        if not root2:
            return root1

        root1.val += root2.val

        root1.left = self.mergeTreesAlt2(root1.left, root2.left)
        root1.right = self.mergeTreesAlt2(root1.right, root2.right)

        return root1


# -------------------------
# Helper Functions for Testing
# -------------------------

def build_tree(arr):
    if not arr:
        return None

    nodes = [None if v is None else TreeNode(v) for v in arr]
    kids = nodes[::-1]
    root = kids.pop()

    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()

    return root


def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


# -------------------------
# Examples (Not From LeetCode)
# -------------------------

# Example 1: Simple merge
t1 = build_tree([1, 3, 2])
t2 = build_tree([2, 1, 3])
# Expected inorder: [4, 3, 5]
print(inorder(Solution().mergeTrees(t1, t2)))


# Example 2: One tree empty
t3 = None
t4 = build_tree([5, 2, 7])
# Expected inorder: [2, 5, 7]
print(inorder(Solution().mergeTrees(t3, t4)))


# Example 3: Uneven trees
t5 = build_tree([4, 1, None, 3])
t6 = build_tree([2, None, 5])
# Expected inorder: [3, 5, 5]
print(inorder(Solution().mergeTrees(t5, t6)))

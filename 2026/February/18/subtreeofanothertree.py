# LeetCode 572: Subtree of Another Tree
# Explanation:
# 1. Given two binary trees s and t, check whether t is a subtree of s.
# 2. Approach:
#    - For each node in s, check if the subtree rooted at that node is identical to t.
#    - Use DFS and a helper function to compare two trees for equality.
# 3. Time Complexity: O(m*n) worst-case, m = nodes in s, n = nodes in t
# 4. Space Complexity: O(h), h = height of s (recursive stack)

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val: int=0, left: Optional['TreeNode']=None, right: Optional['TreeNode']=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # -------------------------------------------------------
    # Method 1: DFS + check equality
    # -------------------------------------------------------
    def isSubtree(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:

        def isSame(a: Optional[TreeNode], b: Optional[TreeNode]) -> bool:
            if not a and not b:
                return True
            if not a or not b:
                return False
            return a.val == b.val and isSame(a.left, b.left) and isSame(a.right, b.right)

        if not s:
            return False
        if isSame(s, t):
            return True
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

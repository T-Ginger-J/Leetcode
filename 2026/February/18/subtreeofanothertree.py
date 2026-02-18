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

    # -------------------------------------------------------
    # Method 2: Serialize trees (preorder) and use substring check
    # -------------------------------------------------------
    def isSubtreeSerialized(self, s: Optional[TreeNode], t: Optional[TreeNode]) -> bool:
        def preorder(node: Optional[TreeNode]) -> str:
            if not node:
                return "#"
            return f",{node.val},{preorder(node.left)},{preorder(node.right)}"
        return preorder(str(t)) in preorder(str(s))


# -------------------------------------------------------
# Examples & Edge Cases
# -------------------------------------------------------

sol = Solution()

# Example 1
s1 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
t1 = TreeNode(4, TreeNode(1), TreeNode(2))
print(sol.isSubtree(s1, t1))           # True

# Example 2: not a subtree
s2 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
t2 = TreeNode(4, TreeNode(1), TreeNode(2))
print(sol.isSubtree(s2, t2))           # False

# Example 3: identical trees
s3 = TreeNode(1)
t3 = TreeNode(1)
print(sol.isSubtree(s3, t3))           # True

# Example 4: t is None
s4 = TreeNode(1)
t4 = None
print(sol.isSubtree(s4, t4))           # False

# Example 5: s is None
s5 = None
t5 = TreeNode(1)
print(sol.isSubtree(s5, t5))           # False

from typing import Optional

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

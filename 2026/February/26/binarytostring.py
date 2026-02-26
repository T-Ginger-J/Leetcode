from typing import Optional


class Solution:

    def tree2str(self, root: Optional[TreeNode]) -> str:

        if not root:
            return ""

        left_str = self.tree2str(root.left)
        right_str = self.tree2str(root.right)

        if right_str:
            return f"{root.val}({left_str})({right_str})"
        elif left_str:
            return f"{root.val}({left_str})"
        else:
            return f"{root.val}"


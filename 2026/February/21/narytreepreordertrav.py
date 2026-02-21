from typing import List

class Solution:

    # -------------------------------------------------------
    # Method 1: DFS recursion
    # -------------------------------------------------------
    def preorder(self, root: 'Node') -> List[int]:
        res = []
        def dfs(node):
            if not node:
                return
            res.append(node.val)
            for child in node.children:
                dfs(child)
        dfs(root)
        return res

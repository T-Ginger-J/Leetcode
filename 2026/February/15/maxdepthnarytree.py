from typing import List, Optional
from collections import deque

class Solution:

    # -------------------------------------------------------
    # Method 1: DFS (recursive)
    # -------------------------------------------------------
    def maxDepth(self, root: Optional[Node]) -> int:
        if not root:
            return 0
        if not root.children:
            return 1
        return 1 + max(self.maxDepth(child) for child in root.children)


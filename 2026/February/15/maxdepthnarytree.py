# LeetCode 559: Maximum Depth of N-ary Tree
# Explanation:
# 1. Given an n-ary tree, find its maximum depth.
# 2. Approach:
#    - DFS: recursively find the max depth among all children and add 1.
#    - BFS: level-order traversal, increment depth at each level.
# 3. Time Complexity: O(n), n = number of nodes
# 4. Space Complexity: O(h) for DFS, O(w) for BFS (h=height, w=width)

from typing import List, Optional
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []

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


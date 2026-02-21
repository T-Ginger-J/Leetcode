# LeetCode 589: N-ary Tree Preorder Traversal
# Explanation:
# 1. Given an n-ary tree, return its nodes' values in preorder (root -> children left to right).
# 2. Approach:
#    - Method 1: DFS recursion
#    - Method 2: Iterative using stack
# 3. Time Complexity: O(n), n = number of nodes
# 4. Space Complexity: O(n) for recursion stack or explicit stack

from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

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

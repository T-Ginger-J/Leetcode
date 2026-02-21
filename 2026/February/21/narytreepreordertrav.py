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

    # -------------------------------------------------------
    # Method 2: Iterative stack
    # -------------------------------------------------------
    def preorderIterative(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            node = stack.pop()
            res.append(node.val)
            # add children in reverse order to visit left to right
            stack.extend(reversed(node.children))
        return res


# -------------------------------------------------------
# Examples & Edge Cases
# -------------------------------------------------------

sol = Solution()

# Example 1: simple tree
root1 = Node(1, [Node(3,[Node(5),Node(6)]), Node(2), Node(4)])
print(sol.preorder(root1))           # [1,3,5,6,2,4]
print(sol.preorderIterative(root1))  # [1,3,5,6,2,4]

# Example 2: single node
root2 = Node(10)
print(sol.preorder(root2))           # [10]

# Example 3: empty tree
root3 = None
print(sol.preorder(root3))           # []

# Example 4: deeper tree
root4 = Node(1, [Node(2,[Node(3,[Node(4)])])])
print(sol.preorderIterative(root4))  # [1,2,3,4]

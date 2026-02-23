# LeetCode 590: N-ary Tree Postorder Traversal
# Explanation:
# 1. Given an n-ary tree, return its nodes' values in postorder (children -> root).
# 2. Postorder traversal visits:
#    - All children from left to right
#    - Then the current node.
# 3. We use two approaches:
#    - Recursive DFS
#    - Iterative using stack (reverse preorder technique)
# 4. Time Complexity: O(n), where n is the number of nodes
# 5. Space Complexity: O(n) for recursion stack or explicit stack

from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children else []


class Solution:

    # -------------------------------------------------------
    # Method 1: Recursive DFS
    # -------------------------------------------------------
    def postorder(self, root: 'Node') -> List[int]:
        res = []

        def dfs(node):
            if not node:
                return
            for child in node.children:
                dfs(child)
            res.append(node.val)

        dfs(root)
        return res

    # -------------------------------------------------------
    # Method 2: Iterative (Reverse Preorder)
    # -------------------------------------------------------
    def postorderIterative(self, root: 'Node') -> List[int]:
        if not root:
            return []

        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            res.append(node.val)

            for child in node.children:
                stack.append(child)

        # Reverse to get postorder
        return res[::-1]


# -------------------------------------------------------
# Examples & Edge Cases
# -------------------------------------------------------

sol = Solution()

# Example 1: Standard tree
root1 = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
print(sol.postorder(root1))           # [5,6,3,2,4,1]
print(sol.postorderIterative(root1))  # [5,6,3,2,4,1]

# Example 2: Single node
root2 = Node(10)
print(sol.postorder(root2))           # [10]

# Example 3: Empty tree
root3 = None
print(sol.postorder(root3))           # []

# Example 4: Deep chain
root4 = Node(1, [Node(2, [Node(3, [Node(4)])])])
print(sol.postorderIterative(root4))  # [4,3,2,1]

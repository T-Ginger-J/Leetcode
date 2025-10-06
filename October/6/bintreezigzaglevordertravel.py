# LeetCode 103: Binary Tree Zigzag Level Order Traversal
# Explanation:
# 1. Similar to normal level order traversal (BFS), but alternate direction per level.
# 2. Use a flag to reverse every other level.
# 3. Append each level’s values to results accordingly.
# Time Complexity: O(n), where n = number of nodes.
# Space Complexity: O(n), for queue and result storage.

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: TreeNode):
        if not root:
            return []
        result, queue, left_to_right = [], deque([root]), True
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if not left_to_right:
                level.reverse()
            result.append(level)
            left_to_right = not left_to_right
        return result
    

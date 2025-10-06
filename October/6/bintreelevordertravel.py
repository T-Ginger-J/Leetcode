# LeetCode 102: Binary Tree Level Order Traversal
# Explanation:
# 1. Use a queue (BFS) to traverse level by level.
# 2. For each level, collect node values before moving to the next level.
# 3. Append each level’s list to the result.
# Time Complexity: O(n), where n = number of nodes.
# Space Complexity: O(n), for the queue and output list.

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        result, queue = [], deque([root])
        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result

    def levelOrderDFS(self, root: TreeNode):
        levels = []
        def dfs(node, level):
            if not node:
                return
            if len(levels) == level:
                levels.append([])
            levels[level].append(node.val)
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        dfs(root, 0)
        return levels
    
# Example 1
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))
print(Solution().levelOrder(root))  # [[3], [9, 20], [15, 7]]

# Example 2
root = TreeNode(1)
print(Solution().levelOrder(root))  # [[1]]

# Example 3
print(Solution().levelOrder(None))  # []

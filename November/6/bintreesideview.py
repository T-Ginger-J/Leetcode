# LeetCode 199: Binary Tree Right Side View
# Explanation:
# 1. Use BFS level-order traversal.
# 2. For each level, add the last node's value to result.
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import deque

class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == level_size - 1:
                    result.append(node.val)
        return result

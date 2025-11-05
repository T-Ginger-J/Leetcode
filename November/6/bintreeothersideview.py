# Custom Problem: Binary Tree Left Side View
# Explanation:
# 1. Use BFS (level-order traversal).
# 2. For each level, record the first node's value (visible from left).
# Time Complexity: O(n)
# Space Complexity: O(n)

from collections import deque

class Solution:
    def leftSideView(self, root):
        if not root:
            return []
        queue = deque([root])
        result = []
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == 0:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result

# Helper tree construction
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
sol = Solution()
print(sol.leftSideView(root))  # [1, 2, 5]

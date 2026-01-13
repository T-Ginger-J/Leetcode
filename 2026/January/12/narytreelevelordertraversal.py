# LeetCode 429: N-ary Tree Level Order Traversal
# Explanation:
# 1. Use BFS to traverse the tree level by level.
# 2. For each level, collect all node values into a list.
# 3. Append each level's list to the final result.

from collections import deque
from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            level = []
            
            for _ in range(level_size):
                node = queue.popleft()
                level.append(node.val)
                queue.extend(node.children)
            
            result.append(level)
        
        return result


from typing import Optional
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], target: int) -> int:
        count = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1  # base case
        
        def dfs(node, curr_sum):
            nonlocal count
            if not node:
                return
            curr_sum += node.val
            count += prefix_sum[curr_sum - target]
            prefix_sum[curr_sum] += 1
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            prefix_sum[curr_sum] -= 1  # backtrack
        
        dfs(root, 0)
        return count


# LeetCode 437: Path Sum III
# Explanation:
# 1. Count the number of paths in a binary tree that sum to a target value.
# 2. Paths must go downward but can start and end anywhere.
# 3. Use DFS with a prefix sum hash map to track cumulative sums efficiently.

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

# Example 1
root = TreeNode(10, 
                TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))),
                TreeNode(-3, None, TreeNode(11)))
target = 8
# Output: 3
print(Solution().pathSum(root, target))

# Example 2
root = TreeNode(1)
target = 0
# Output: 0
print(Solution().pathSum(root, target))

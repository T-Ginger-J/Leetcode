# LeetCode 95: Unique Binary Search Trees II
# Explanation:
# 1. Generate all unique BSTs that store values 1...n.
# 2. Use recursion with divide and conquer:
#    - For each number i in 1..n:
#      - Treat i as root.
#      - Recursively generate all left subtrees from [1..i-1].
#      - Recursively generate all right subtrees from [i+1..n].
#    - Combine every left and right subtree pair with i as root.
# 3. Base case: if start > end, return [None].
# Time Complexity: O(Cn), where Cn is the nth Catalan number (~O(4^n / n^(3/2))).
# Space Complexity: O(Cn).

from typing import List, Optional
from functools import lru_cache

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        
        def build(start, end):
            if start > end:
                return [None]
            trees = []
            for i in range(start, end + 1):
                for left in build(start, i - 1):
                    for right in build(i + 1, end):
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        trees.append(root)
            return trees
        
        return build(1, n)

    def generateTreesOptimized(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        @lru_cache(None)
        def build(start, end):
            if start > end:
                return [None]
            trees = []
            for i in range(start, end + 1):
                for left in build(start, i - 1):
                    for right in build(i + 1, end):
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        trees.append(root)
            return trees

        return build(1, n)
    
    def generateTreesOneLine(self, n: int):
        def f(a, b): 
            return [TreeNode(i, l, r) for i in range(a, b+1) for l in f(a, i-1) for r in f(i+1, b)] or [None]
        return f(1, n)
    
    # Helper to print tree preorder
def preorder(root):
    return [root.val] + preorder(root.left) + preorder(root.right) if root else []

# Example 1
trees = Solution().generateTrees(3)
for t in trees:
    print(preorder(t))
# Possible outputs (different BST structures):
# [1, None, 2, None, 3]
# [1, None, 3, 2]
# [2, 1, 3]
# [3, 1, None, None, 2]
# [3, 2, None, 1]

# Example 2
print(len(Solution().generateTrees(1)))  # 1

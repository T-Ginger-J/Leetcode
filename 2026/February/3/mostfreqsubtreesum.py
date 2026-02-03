# LeetCode 508: Most Frequent Subtree Sum
# Explanation:
# Given the root of a binary tree, compute the sum of each subtree.
# Return all subtree sums that occur most frequently.
#
# Method 1: Postorder DFS + Hash Map (Optimal)
# - Postorder traversal ensures children are processed before parent.
# - Compute subtree sum = left + right + node.val.
# - Count frequencies using a hash map.
# - Track the maximum frequency and return all sums with that frequency.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import Optional, List
from collections import defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        freq = defaultdict(int)
        max_freq = 0

        def dfs(node):
            nonlocal max_freq
            if not node:
                return 0
            s = dfs(node.left) + dfs(node.right) + node.val
            freq[s] += 1
            max_freq = max(max_freq, freq[s])
            return s

        dfs(root)
        return [s for s, c in freq.items() if c == max_freq]


# Alternate Python Solution: Two-Pass DFS
# - First pass computes subtree sums and stores them.
# - Second pass counts frequencies and extracts max.

class SolutionTwoPass:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        sums = []

        def dfs(node):
            if not node:
                return 0
            s = dfs(node.left) + dfs(node.right) + node.val
            sums.append(s)
            return s

        dfs(root)

        freq = defaultdict(int)
        for s in sums:
            freq[s] += 1

        max_freq = max(freq.values())
        return [s for s, c in freq.items() if c == max_freq]


# Additional Examples (Edge Cases and Non-LeetCode Examples)

# Helper to build tree from level-order list
def build_tree(vals):
    if not vals:
        return None
    nodes = [None if v is None else TreeNode(v) for v in vals]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

sol = Solution()

# Example 1: Single node
root1 = build_tree([5])
print(sol.findFrequentTreeSum(root1))
# Expected output: [5]

# Example 2: Multiple frequent sums
root2 = build_tree([5,2,-3])
print(sol.findFrequentTreeSum(root2))
# Expected output: [2, -3, 4]

# Example 3: All zero values
root3 = build_tree([0,0,0])
print(sol.findFrequentTreeSum(root3))
# Expected output: [0]

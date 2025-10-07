# LeetCode 106: Construct Binary Tree from Inorder and Postorder Traversal
# Explanation:
# 1. Postorder: [Left, Right, Root] — the last element is always the root.
# 2. Inorder: [Left, Root, Right] — find the root’s position to divide subtrees.
# 3. Build right subtree first (since postorder pops from end).
# 4. Use a hashmap for O(1) root index lookup in inorder.
# Time Complexity: O(n)
# Space Complexity: O(n)

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index_map = {val: i for i, val in enumerate(inorder)}
        self.post_idx = len(postorder) - 1

        def helper(left, right):
            if left > right:
                return None
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(root_val)
            index = index_map[root_val]
            root.right = helper(index + 1, right)
            root.left = helper(left, index - 1)
            return root

        return helper(0, len(inorder) - 1)

    def buildTreeOneLine(self, I, P):
        if not I: return None
        x = P.pop()
        i = I.index(x)
        return TreeNode(x, self.buildTree(I[:i], P), self.buildTree(I[i+1:], P))

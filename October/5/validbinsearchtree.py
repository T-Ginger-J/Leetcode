# LeetCode 98: Validate Binary Search Tree
# Explanation:
# 1. A valid BST satisfies: 
#    - Left subtree < root < Right subtree.
#    - Both subtrees must also be valid BSTs.
# 2. Use recursion with range limits (min_val, max_val) to validate each node.
# 3. Each node’s value must be strictly between the allowed range.
# Time Complexity: O(n), where n = number of nodes.
# Space Complexity: O(h), where h = tree height (recursion stack).


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low=float('-inf'), high=float('inf')):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)
        return validate(root)

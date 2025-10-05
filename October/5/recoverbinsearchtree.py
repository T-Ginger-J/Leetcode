# LeetCode 99: Recover Binary Search Tree
# Explanation:
# 1. Two nodes in a BST are swapped by mistake.
# 2. Use inorder traversal — values should be in ascending order.
# 3. When order breaks (prev.val > curr.val), mark those two nodes.
# 4. After traversal, swap their values to fix the BST.
# Time Complexity: O(n)
# Space Complexity: O(h) (recursion stack)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        self.first = self.second = self.prev = None
        
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev and self.prev.val > node.val:
                if not self.first:
                    self.first = self.prev
                self.second = node
            self.prev = node
            inorder(node.right)
        
        inorder(root)
        self.first.val, self.second.val = self.second.val, self.first.val

    def recoverTreeOptimized(self, root: TreeNode) -> None:
        first = second = prev = None
        cur = root
        while cur:
            if not cur.left:
                if prev and prev.val > cur.val:
                    if not first:
                        first = prev
                    second = cur
                prev = cur
                cur = cur.right
            else:
                pre = cur.left
                while pre.right and pre.right != cur:
                    pre = pre.right
                if not pre.right:
                    pre.right = cur
                    cur = cur.left
                else:
                    pre.right = None
                    if prev and prev.val > cur.val:
                        if not first:
                            first = prev
                        second = cur
                    prev = cur
                    cur = cur.right
        first.val, second.val = second.val, first.val

# Build invalid BST: [1,3,null,null,2]
root = TreeNode(1)
root.left = TreeNode(3)
root.left.right = TreeNode(2)

Solution().recoverTree(root)

# Validate recovery
def inorder(root):
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []
print(inorder(root))  # [1,2,3]

# Example 2
root = TreeNode(3, TreeNode(1), TreeNode(4, TreeNode(2)))
Solution().recoverTree(root)
print(inorder(root))  # [1,2,3,4]

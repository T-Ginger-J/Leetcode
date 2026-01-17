# LeetCode 449: Serialize and Deserialize BST
# Explanation:
# Implement a codec to serialize and deserialize a Binary Search Tree (BST).
# - Serialization: convert BST to a string
# - Deserialization: reconstruct BST from the string
#
# Method 1: Preorder Traversal with Bounds (Optimal for BST)
# - Serialize: preorder traversal with space-separated values
# - Deserialize: use BST property with min/max bounds for placement
#
# Time Complexity: O(n)
# Space Complexity: O(n) (recursion stack + string storage)

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def preorder(node):
            if not node:
                return
            res.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return ' '.join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        preorder = list(map(int, data.split()))
        index = 0
        
        def build(min_val, max_val):
            nonlocal index
            if index == len(preorder):
                return None
            val = preorder[index]
            if val < min_val or val > max_val:
                return None
            index += 1
            node = TreeNode(val)
            node.left = build(min_val, val)
            node.right = build(val, max_val)
            return node
        
        return build(float('-inf'), float('inf'))

# Helper function to print inorder traversal
def inorder(node):
    return inorder(node.left) + [node.val] + inorder(node.right) if node else []

# Additional Examples (Edge Cases and Non-LeetCode Examples)

codec = Codec()

# Example 1: Simple BST
root1 = TreeNode(2, TreeNode(1), TreeNode(3))
data1 = codec.serialize(root1)
print(data1)               # Expected output: "2 1 3"
print(inorder(codec.deserialize(data1)))  # Expected: [1,2,3]

# Example 2: BST with only left children
root2 = TreeNode(3, TreeNode(2, TreeNode(1)))
dat

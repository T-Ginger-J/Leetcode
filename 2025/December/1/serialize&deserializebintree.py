# LeetCode 297: Serialize and Deserialize Binary Tree
# Explanation:
# We use BFS for both serialization and deserialization.
# - serialize(): Perform level-order traversal, append "null" for missing nodes.
# - deserialize(): Reverse process by reconstructing using queue.
#
# Time Complexity:
#   • serialize():  O(n)
#   • deserialize(): O(n)
# Space Complexity: O(n) to store serialized list and queue.

from collections import deque

class Codec:

    def serialize(self, root):
        if not root: 
            return "null"
        q = deque([root])
        res = []
        while q:
            node = q.popleft()
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("null")
        return ",".join(res)

    def deserialize(self, data):
        if data == "null":
            return None
        vals = data.split(",")
        root = TreeNode(int(vals[0]))
        q = deque([root])
        i = 1
        while q:
            node = q.popleft()
            if vals[i] != "null":
                node.left = TreeNode(int(vals[i]))
                q.append(node.left)
            i += 1
            if vals[i] != "null":
                node.right = TreeNode(int(vals[i]))
                q.append(node.right)
            i += 1
        return root

codec = Codec()
root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))

s = codec.serialize(root)
print(s)  
# Example output: "1,2,3,null,null,4,5,null,null,null,null"

tree = codec.deserialize(s)
print(codec.serialize(tree))  # Should match original serialization

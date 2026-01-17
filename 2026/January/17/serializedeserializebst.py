from typing import Optional

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

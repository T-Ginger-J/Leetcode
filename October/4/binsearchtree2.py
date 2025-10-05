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

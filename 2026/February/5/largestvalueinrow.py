
class Solution:

    # -------------------------------------------------------
    # Method 1: BFS
    # -------------------------------------------------------
    def largestValuesBFS(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        res = []
        queue = deque([root])

        while queue:

            size = len(queue)
            max_val = float('-inf')

            for _ in range(size):
                node = queue.popleft()
                max_val = max(max_val, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            res.append(max_val)

        return res


# LeetCode 257: Binary Tree Paths
#
# Explanation:
# Use DFS:
# - Build a path string while traversing down the tree.
# - When reaching a leaf, append the full path to the result list.
#
# Time Complexity: O(n) — visit every node once
# Space Complexity: O(h) recursion stack, h = tree height

class Solution:
    def binaryTreePaths(self, root):
        res = []

        def dfs(node, path):
            if not node:
                return
            if not node.left and not node.right:  # leaf
                res.append(path + str(node.val))
                return
            dfs(node.left, path + str(node.val) + "->")
            dfs(node.right, path + str(node.val) + "->")

        dfs(root, "")
        return res

# Example usage:
# sol = Solution()
# print(sol.binaryTreePaths(root))  # e.g. ["1->2->5","1->3"]


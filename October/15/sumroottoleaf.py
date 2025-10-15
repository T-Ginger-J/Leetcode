# LeetCode 129: Sum Root to Leaf Numbers
# Explanation:
# 1. Each root-to-leaf path represents a number formed by concatenating node values.
# 2. Use DFS to traverse the tree, carrying the current number as you go.
# 3. When a leaf node is reached, add its number to the total sum.
# Time Complexity: O(n), where n = number of nodes.
# Space Complexity: O(h), where h = height of the tree (recursion stack).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def dfs(node, curr_sum):
            if not node:
                return 0
            curr_sum = curr_sum * 10 + node.val
            if not node.left and not node.right:
                return curr_sum
            return dfs(node.left, curr_sum) + dfs(node.right, curr_sum)
        return dfs(root, 0)

    def sumNumbersIterative(self, root: TreeNode) -> int:
        if not root:
            return 0
        total = 0
        queue = deque([(root, root.val)])
        while queue:
            node, curr = queue.popleft()
            if not node.left and not node.right:
                total += curr
            if node.left:
                queue.append((node.left, curr * 10 + node.left.val))
            if node.right:
                queue.append((node.right, curr * 10 + node.right.val))
        return total

    def sumNumbersOneLine(self, r):
        return 0 if not r else (r.val if not r.left and not r.right else self.sumNumbers(r.left and TreeNode(r.left.val+10*r.val,r.left.left,r.left.right))+self.sumNumbers(r.right and TreeNode(r.right.val+10*r.val,r.right.left,r.right.right)))
    
# Tree: [1, 2, 3]
# Paths: 12 + 13 = 25
root = TreeNode(1, TreeNode(2), TreeNode(3))
print(Solution().sumNumbers(root))
# Output: 25

# Tree: [4, 9, 0, 5, 1]
# Paths: 495 + 491 + 40 = 1026
root = TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0))
print(Solution().sumNumbers(root))
# Output: 1026


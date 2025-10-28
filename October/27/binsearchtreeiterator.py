# LeetCode 173: Binary Search Tree Iterator
# Explanation:
# 1. Perform an in-order traversal (Left → Node → Right) to get sorted order.
# 2. Use a stack to simulate recursion and fetch next smallest element on demand.
# 3. `next()` pops the smallest node and explores its right subtree.
# 4. `hasNext()` checks if more elements remain.
# Time Complexity: O(1) amortized per operation
# Space Complexity: O(h) where h is tree height

class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._push_left(root)
    
    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        node = self.stack.pop()
        val = node.val
        if node.right:
            self._push_left(node.right)
        return val

    def hasNext(self):
        return len(self.stack) > 0

# Assume TreeNode class is defined as usual in LeetCode.
root = TreeNode(7, TreeNode(3), TreeNode(15, TreeNode(9), TreeNode(20)))
iterator = BSTIterator(root)
print(iterator.next())     # 3
print(iterator.next())     # 7
print(iterator.hasNext())  # True
print(iterator.next())     # 9
print(iterator.hasNext())  # True
print(iterator.next())     # 15
print(iterator.hasNext())  # True
print(iterator.next())     # 20
print(iterator.hasNext())  # False

# LeetCode 108: Convert Sorted Array to Binary Search Tree
# Explanation:
# 1. Given a sorted array, we can create a height-balanced BST by choosing the middle element as the root.
# 2. Recursively assign the middle of the left half as the left subtree and the middle of the right half as the right subtree.
# 3. This ensures the BST is balanced and maintains sorted order.
# Time Complexity: O(n)
# Space Complexity: O(log n) for recursion stack (balanced tree height).

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = helper(left, mid - 1)
            root.right = helper(mid + 1, right)
            return root
        return helper(0, len(nums) - 1)

    def sortedArrayToBSTOneLine(self, A):
        return None if not A else TreeNode(A[len(A)//2], self.sortedArrayToBST(A[:len(A)//2]), self.sortedArrayToBST(A[len(A)//2+1:]))

print(Solution().sortedArrayToBST([-10, -3, 0, 5, 9]).val)  # 0
print(Solution().sortedArrayToBST([1, 3]).val)              # 3 or 1 (balanced tree)
print(Solution().sortedArrayToBST([]))                      # None

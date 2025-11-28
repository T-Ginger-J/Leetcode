# LeetCode 307: Range Sum Query - Mutable
# Explanation:
# 1. Use a segment tree to support both update and sumRange in O(log n).
# 2. Each tree node represents the sum of a segment.
# 3. update(index, val): update value and propagate changes up.
# 4. sumRange(left, right): query sum recursively using the tree.
# Time Complexity: O(log n) per update and query
# Space Complexity: O(n) for segment tree

class NumArray:

    def __init__(self, nums):
        if not nums: 
            self.nums = []
            return
        self.n = len(nums)
        self.tree = [0] * (2*self.n)
        # build the tree
        for i in range(self.n):
            self.tree[self.n + i] = nums[i]
        for i in range(self.n-1, 0, -1):
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    def update(self, index: int, val: int) -> None:
        i = index + self.n
        self.tree[i] = val
        while i > 1:
            i //= 2
            self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

    def sumRange(self, left: int, right: int) -> int:
        l, r = left + self.n, right + self.n
        s = 0
        while l <= r:
            if l % 2 == 1:
                s += self.tree[l]
                l += 1
            if r % 2 == 0:
                s += self.tree[r]
                r -= 1
            l //= 2
            r //= 2
        return s

nums = [1, 3, 5]
obj = NumArray(nums)
print(obj.sumRange(0, 2)) # 9
obj.update(1, 2)
print(obj.sumRange(0, 2)) # 8

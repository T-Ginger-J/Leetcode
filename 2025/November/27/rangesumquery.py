# LeetCode 303: Range Sum Query - Immutable
# Explanation:
# 1. Precompute prefix sums for the array.
# 2. sumRange(i, j) = prefix[j+1] - prefix[i].
# Time Complexity: O(n) for precomputation, O(1) per query
# Space Complexity: O(n) for storing prefix sums

class NumArray:

    def __init__(self, nums):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]

nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
print(obj.sumRange(0, 2))  # 1
print(obj.sumRange(2, 5))  # -1
print(obj.sumRange(0, 5))  # -3

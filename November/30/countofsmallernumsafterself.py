# LeetCode 315: Count of Smaller Numbers After Self
# Explanation:
# 1. Use a Binary Indexed Tree (Fenwick Tree) to count smaller elements efficiently.
# 2. Discretize the numbers to indices because BIT works on indices.
# 3. Traverse nums from right to left:
#    - query BIT for count of elements smaller than current
#    - update BIT with current element
# Time Complexity: O(n log n) due to BIT operations
# Space Complexity: O(n) for BIT and mapping

from bisect import bisect_left, insort

class Solution:
    def countSmaller(self, nums):
        offset = abs(min(nums)) + 1  # shift negatives
        size = max(nums) + offset + 1
        bit = [0] * size

        def update(i):
            while i < size:
                bit[i] += 1
                i += i & -i

        def query(i):
            res = 0
            while i > 0:
                res += bit[i]
                i -= i & -i
            return res

        res = []
        for num in reversed(nums):
            res.append(query(num + offset - 1))
            update(num + offset)
        return res[::-1]


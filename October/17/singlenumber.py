# LeetCode 136: Single Number
# Explanation:
# 1. Every element appears twice except one.
# 2. Use XOR (^) since:
#    - a ^ a = 0
#    - a ^ 0 = a
#    - XOR is commutative and associative.
# 3. Thus, XORing all numbers cancels out pairs and leaves the single one.
# Time Complexity: O(n)
# Space Complexity: O(1)


from functools import reduce
import operator


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res

    def singleNumberOneLine(self, nums: list[int]) -> int:
        return reduce(operator.xor, nums)

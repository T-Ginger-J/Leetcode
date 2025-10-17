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

import random
from collections import defaultdict

class Solution:
    def __init__(self, nums: list[int]):
        self.nums = nums

    def pick(self, target: int) -> int:
        count = 0
        res = -1
        for i, num in enumerate(self.nums):
            if num == target:
                count += 1
                if random.randint(1, count) == 1:
                    res = i
        return res

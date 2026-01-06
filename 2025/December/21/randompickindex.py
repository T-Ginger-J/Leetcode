# LeetCode 398: Random Pick Index
# Explanation:
# 1. Use reservoir sampling to pick index of target randomly
# 2. Iterate through array, replace answer with probability 1/count
# Time Complexity: O(n) per pick
# Space Complexity: O(1)

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
    
class SolutionPreprocess:
    def __init__(self, nums: list[int]):
        self.indices = defaultdict(list)
        for i, num in enumerate(nums):
            self.indices[num].append(i)

    def pick(self, target: int) -> int:
        # pick a random index from the list
        return random.choice(self.indices[target])

nums = [1,2,3,3,3]
solution = Solution(nums)
print(solution.pick(3))  # Randomly returns 2, 3, or 4
print(solution.pick(1))  # Returns 0

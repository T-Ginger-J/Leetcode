
from typing import List

class Solution:
    # Method 1: Math (Optimal)
    def minMoves(self, nums: List[int]) -> int:
        min_val = min(nums)
        return sum(nums) - min_val * len(nums)

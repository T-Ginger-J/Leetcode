from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)

        for bit in range(32):
            ones = 0
            for num in nums:
                ones += (num >> bit) & 1
            total += ones * (n - ones)

        return total

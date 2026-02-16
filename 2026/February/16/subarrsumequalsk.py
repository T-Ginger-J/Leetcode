from typing import List
from collections import defaultdict

class Solution:

    # -------------------------------------------------------
    # Method 1: Prefix sum + HashMap
    # -------------------------------------------------------
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        cum_sum = 0
        sums = defaultdict(int)
        sums[0] = 1  # empty subarray sum
        for num in nums:
            cum_sum += num
            count += sums.get(cum_sum - k, 0)
            sums[cum_sum] += 1
        return count


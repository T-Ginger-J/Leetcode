# LeetCode 560: Subarray Sum Equals K
# Explanation:
# 1. Given an array nums and integer k, count the total number of continuous subarrays whose sum equals k.
# 2. Approach:
#    - Use prefix sum and hashmap:
#      - Let cum_sum be the cumulative sum up to current index.
#      - If cum_sum - k exists in hashmap, it means a subarray ending at current index sums to k.
#      - Keep track of count of each cumulative sum in hashmap.
# 3. Time Complexity: O(n), n = length of nums
# 4. Space Complexity: O(n), for hashmap

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


from typing import List
from collections import Counter

class Solution:
    # Method 1: Hash Map (Optimal)
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        ab_sum = Counter()
        for a in A:
            for b in B:
                ab_sum[a + b] += 1

        count = 0
        for c in C:
            for d in D:
                count += ab_sum.get(-(c + d), 0)

        return count

from typing import Dict
from collections import Counter

class Solution:
    # Method 1: Bucket Sort
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        buckets = [[] for _ in range(len(s) + 1)]
        for ch, f in freq.items():
            buckets[f].append(ch)

        res = []
        for f in range(len(buckets) - 1, 0, -1):
            for ch in buckets[f]:
                res.append(ch * f)
        return "".join(res)


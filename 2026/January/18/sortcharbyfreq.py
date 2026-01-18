# LeetCode 451: Sort Characters By Frequency
# Explanation:
# Given a string s, sort it in decreasing order based on the frequency of characters.
#
# Method 1: Bucket Sort by Frequency (Optimal)
# - Count frequency of each character.
# - Create buckets where index = frequency.
# - Place characters into buckets and build result from high to low frequency.
#
# Time Complexity: O(n)
# Space Complexity: O(n)
#
# Method 2: Heap (Alternative)
# - Use a max-heap based on frequency.
#
# Time Complexity: O(n log k), k = number of unique characters
# Space Complexity: O(k)

from typing import Dict
from collections import Counter
import heapq

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

    # Method 2: Heap
    def frequencySortHeap(self, s: str) -> str:
        freq = Counter(s)
        heap = [(-f, ch) for ch, f in freq.items()]
        heapq.heapify(heap)

        res = []
        while heap:
            f, ch = heapq.heappop(heap)
            res.append(ch * (-f))
        return "".join(res)

# LeetCode 436: Find Right Interval
# Explanation:
# 1. For each interval, find the interval with the smallest start >= current interval's end.
# 2. Use sorting and binary search for efficient lookup.

from typing import List
import bisect

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        # Store original indices
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))
        result = [-1] * n
        
        for i, interval in enumerate(intervals):
            end = interval[1]
            # Binary search for the smallest start >= end
            idx = bisect.bisect_left(starts, (end, 0))
            if idx < n:
                result[i] = starts[idx][1]
        
        return result

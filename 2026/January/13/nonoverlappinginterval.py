# LeetCode 435: Non-overlapping Intervals
# Explanation:
# 1. Sort intervals by their end times.
# 2. Greedily select intervals that do not overlap with the previous selected interval.
# 3. Count the number of intervals to remove = total - max non-overlapping intervals.

from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort by end time
        intervals.sort(key=lambda x: x[1])
        count = 0
        prev_end = float('-inf')
        
        for interval in intervals:
            if interval[0] >= prev_end:
                prev_end = interval[1]
            else:
                # Overlapping interval, remove it
                count += 1
        
        return count

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

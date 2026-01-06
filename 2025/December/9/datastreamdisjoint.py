# LeetCode 352: Data Stream as Disjoint Intervals
# Explanation:
# 1. Use SortedDict to keep intervals sorted by start.
# 2. When adding a number, check if it can merge with previous/next intervals.
# 3. getIntervals() returns the current list of intervals.
# Time Complexity: addNum O(log n), getIntervals O(n)
# Space Complexity: O(n)

from sortedcontainers import SortedDict

class SummaryRanges:
    def __init__(self):
        self.intervals = SortedDict()
    
    def addNum(self, val: int) -> None:
        if val in self.intervals:
            return
        
        keys = self.intervals.keys()
        left = right = val
        
        # Merge with previous interval if adjacent
        idx = self.intervals.bisect_left(val)
        if idx != 0 and self.intervals[keys[idx-1]] + 1 >= val:
            idx -= 1
            left = keys[idx]
            right = max(self.intervals[keys[idx]], right)
            del self.intervals[keys[idx]]
        
        # Merge with next intervals if adjacent
        while idx < len(self.intervals) and self.intervals.keys()[idx] <= right + 1:
            right = max(right, self.intervals.pop(self.intervals.keys()[idx]))
        
        self.intervals[left] = right

    def getIntervals(self) -> list[list[int]]:
        return [[k, v] for k, v in self.intervals.items()]

sr = SummaryRanges()
sr.addNum(1)
print(sr.getIntervals())  # Output: [[1,1]]
sr.addNum(3)
print(sr.getIntervals())  # Output: [[1,1],[3,3]]
sr.addNum(2)
print(sr.getIntervals())  # Output: [[1,3]]
sr.addNum(7)
print(sr.getIntervals())  # Output: [[1,3],[7,7]]

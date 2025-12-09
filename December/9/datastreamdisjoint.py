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

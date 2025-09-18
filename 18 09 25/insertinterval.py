class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        res = []
        for i, (s, e) in enumerate(intervals):
            if newInterval[1] < s:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > e:
                res.append([s, e])
            else:
                newInterval = [min(newInterval[0], s), max(newInterval[1], e)]
        res.append(newInterval)
        return res
    

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
    

s = Solution()
print(s.insert([[1,3],[6,9]], [2,5]))          # [[1,5],[6,9]]
print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))  # [[1,2],[3,10],[12,16]]

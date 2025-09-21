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
    
    insertOneLine=lambda A,I:__import__('functools').reduce(lambda a,x:a+[x] if I[1]<x[0] and not a.append(I) else a if I[0]>x[1] or not a.append([min(I[0],x[0]),max(I[1],x[1])]) or not I.pop() else a,[x for x in A],[ ])+([I] if I else [])


s = Solution()
print(s.insert([[1,3],[6,9]], [2,5]))          # [[1,5],[6,9]]
print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))  # [[1,2],[3,10],[12,16]]

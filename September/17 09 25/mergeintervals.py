#O(nlogn)

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        return merged

    def mergeOneLine(self, intervals: list[list[int]]) -> list[list[int]]:
        return __import__('functools').reduce(lambda m, x: m[:-1]+[[m[-1][0], max(m[-1][1], x[1])]] if x[0] <= m[-1][1] else m+[x], sorted(intervals), [sorted(intervals)[0]])
    
# ---- Example Usage ----
sol = Solution()

print(sol.merge([[1,3],[2,6],[8,10],[15,18]]))
# Output: [[1,6],[8,10],[15,18]]

print(sol.merge([[1,4],[4,5]]))
# Output: [[1,5]]

print(sol.merge([[1,2],[3,4],[5,6]]))
# Output: [[1,2],[3,4],[5,6]]

print(sol.merge([[1,10],[2,3],[4,5],[6,7]]))
# Output: [[1,10]]

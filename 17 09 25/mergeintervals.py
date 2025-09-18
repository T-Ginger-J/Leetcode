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

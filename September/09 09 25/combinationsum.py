#O(n^2)
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start: int, path: List[int], total: int):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                # not i + 1 because we can reuse the same element
                backtrack(i, path, total + candidates[i])
                path.pop()

        backtrack(0, [], 0)
        return res

    def combinationSumOneLine(self, candidates, target):
        return [[c] + rest for i, c in enumerate(candidates) for rest in self.combinationSum(candidates[i:], target - c)] if target > 0 else ([[]] if target == 0 else [])

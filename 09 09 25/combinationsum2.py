#O(n)
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  # sort to handle duplicates
        res = []

        def backtrack(start: int, path: List[int], total: int):
            if total == target:
                res.append(path[:])
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                # skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] + total > target:
                    break
                path.append(candidates[i])
                backtrack(i + 1, path, total + candidates[i])
                path.pop()

        backtrack(0, [], 0)
        return res

    def combinationSum2OneLine(self, candidates, target):
        candidates.sort()
        return ([[]] if target == 0 else
                [ [c] + rest
                  for i, c in enumerate(candidates)
                  if i == 0 or c != candidates[i-1]
                  for rest in self.combinationSum2(candidates[i+1:], target - c)
                  if target - c >= 0 ])

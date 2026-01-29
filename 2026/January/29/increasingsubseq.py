from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = set()
        
        def dfs(index, path):
            if len(path) >= 2:
                res.add(tuple(path))
            for i in range(index, len(nums)):
                if not path or nums[i] >= path[-1]:
                    dfs(i + 1, path + [nums[i]])
        
        dfs(0, [])
        return list(map(list, res))

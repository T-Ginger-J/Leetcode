#O(n!)
from typing import List
from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtrack(path, remaining):
            if not remaining:
                res.append(path)
                return
            for i in range(len(remaining)):
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])
        
        backtrack([], nums)
        return res
    
    def permuteOneLine(self, nums):
        return list(map(list, permutations(nums)))

sol = Solution()
print(sol.permute([1,2,3]))
# [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

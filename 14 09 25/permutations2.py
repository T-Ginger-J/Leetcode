#O(n!)
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # sort to handle duplicates
        
        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                used[i] = True
                path.append(nums[i])
                backtrack(path, used)
                path.pop()
                used[i] = False
        
        backtrack([], [False]*len(nums))
        return res

sol = Solution()
print(sol.permuteUnique([1,1,2]))
# [[1,1,2],[1,2,1],[2,1,1]]

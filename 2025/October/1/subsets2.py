# LeetCode 90: Subsets II
# Explanation:
# 1. We need all possible subsets of nums (the power set).
# 2. Duplicates must not appear in the result.
# 3. Sort nums first to group duplicates together.
# 4. Use backtracking:
#    - Add current subset to results.
#    - At each step, skip duplicate elements by checking nums[i] == nums[i-1].
# Time Complexity: O(2^n)
# Space Complexity: O(2^n) (for storing results)

from typing import List
import itertools

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        def backtrack(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(0, [])
        return res

    def subsetsWithDupIterative(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        start = 0
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                temp = [curr + [num] for curr in res[start:]]
            else:
                temp = [curr + [num] for curr in res]
            start = len(res)
            res.extend(temp)
        return res
    
    def subsetsWithDupOneLine(self, nums):
        return list(map(list, set(itertools.chain.from_iterable(
            itertools.combinations(sorted(nums), r) for r in range(len(nums)+1)
        ))))
    
# Example 1
print(Solution().subsetsWithDup([1,2,2]))
# [[], [1], [2], [1,2], [2,2], [1,2,2]]

# Example 2
print(Solution().subsetsWithDup([0]))
# [[], [0]]

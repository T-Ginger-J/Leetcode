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

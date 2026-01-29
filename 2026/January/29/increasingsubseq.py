# LeetCode 491: Increasing Subsequences
# Explanation:
# Given an integer array, return all different possible increasing subsequences
# of length at least 2.
#
# Method 1: Backtracking + Set to avoid duplicates
# - Use recursion to try including each number if it keeps the sequence increasing.
# - Use a set to store sequences as tuples to avoid duplicates.
#
# Time Complexity: O(2^n) worst case
# Space Complexity: O(2^n) for result storage

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


# Alternate Python Solution: Backtracking without extra tuple conversion
# - Use a local set per recursion to avoid duplicates at the same level
# - Slightly more memory efficient

class SolutionOptimized:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(start, path):
            if len(path) >= 2:
                res.append(path[:])
            used = set()
            for i in range(start, len(nums)):
                if (not path or nums[i] >= path[-1]) and nums[i] not in used:
                    used.add(nums[i])
                    dfs(i + 1, path + [nums[i]])
        
        dfs(0, [])
        return res


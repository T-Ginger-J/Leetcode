# LeetCode 78: Subsets
# Explanation:
# 1. Use backtracking to explore subsets.
# 2. At each step, include or exclude the current number.
# 3. Collect all paths as valid subsets.
# Time Complexity: O(2^n * n) since each element has two choices.
# Space Complexity: O(n) recursion depth.

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        
        def backtrack(start, path):
            res.append(path[:])
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()
        
        backtrack(0, [])
        return res

# Example usage:
# sol = Solution()
# print(sol.subsets([1,2,3]))  # [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
# print(sol.subsets([0]))      # [[],[0]]

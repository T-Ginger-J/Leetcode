# LeetCode 216: Combination Sum III
# Explanation:
# 1. Use backtracking to explore all combinations of numbers 1–9.
# 2. Each recursive call tries adding a new number to the combination.
# 3. Stop when combination length == k and sum == n.
# Time Complexity: O(C(9, k)) → at most 2^9 = 512 combinations.
# Space Complexity: O(k) recursion depth.

class Solution:
    def combinationSum3(self, k: int, n: int) -> list[list[int]]:
        res = []
        
        def backtrack(start, path, total):
            if len(path) == k:
                if total == n:
                    res.append(path[:])
                return
            for i in range(start, 10):
                if total + i > n: 
                    break
                path.append(i)
                backtrack(i + 1, path, total + i)
                path.pop()
        
        backtrack(1, [], 0)
        return res

sol = Solution()
print(sol.combinationSum3(3, 7))  # [[1,2,4]]
print(sol.combinationSum3(3, 9))  # [[1,2,6],[1,3,5],[2,3,4]]
print(sol.combinationSum3(4, 1))  # []

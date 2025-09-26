# LeetCode 77: Combinations
# Explanation:
# 1. Use backtracking to build combinations.
# 2. At each step, choose a number or skip it.
# 3. Stop when we have k numbers.
# Time Complexity: O(C(n, k) * k) because each combination requires building.
# Space Complexity: O(k) recursion depth.

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        
        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb[:])
                return
            for i in range(start, n + 1):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()
        
        backtrack(1, [])
        return res

    def combinePrune(self, n: int, k: int) -> list[list[int]]:
        res = []
        
        def backtrack(start, comb):
            if len(comb) == k:
                res.append(comb[:])
                return
            for i in range(start, n - (k - len(comb)) + 2):
                comb.append(i)
                backtrack(i + 1, comb)
                comb.pop()
        
        backtrack(1, [])
        return res
    
    combineBuiltIn=lambda s,n,k:__import__('itertools').combinations(range(1,n+1),k)

# Example usage:
# sol = Solution()
# print(sol.combine(4, 2))  # [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]

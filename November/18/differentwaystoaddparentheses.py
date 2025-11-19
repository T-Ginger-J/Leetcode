# LeetCode 241: Different Ways to Add Parentheses
#
# Explanation:
# Use recursion and split the expression at each operator.
# For each operator:
#   - compute all results from left substring
#   - compute all results from right substring
#   - combine them using the operator
#
# Memoization speeds up repeated sub-expressions.
#
# Time Complexity: O(n * 2^n)
# Space Complexity: O(2^n) recursion + memo

class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        memo = {}

        def compute(expr):
            if expr in memo:
                return memo[expr]
            
            results = []
            for i, ch in enumerate(expr):
                if ch in "+-*":
                    left = compute(expr[:i])
                    right = compute(expr[i+1:])
                    for a in left:
                        for b in right:
                            if ch == '+':
                                results.append(a + b)
                            elif ch == '-':
                                results.append(a - b)
                            else:  # '*'
                                results.append(a * b)

            if not results:          # expr is a number
                results = [int(expr)]

            memo[expr] = results
            return results
        
        return compute(expression)

# Example usage:
# sol = Solution()
# print(sol.diffWaysToCompute("2-1-1"))  # [0,2]
# print(sol.diffWaysToCompute("2*3-4*5")) # [-34,-14,-10,-10,10]

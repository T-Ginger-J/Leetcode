# LeetCode 509: Fibonacci Number
# Explanation:
# Compute the nth Fibonacci number where:
# F(0) = 0, F(1) = 1
# F(n) = F(n-1) + F(n-2)
#
# Method 1: Iterative Dynamic Programming (Optimal)
# - Use two variables to keep track of the last two Fibonacci numbers.
# - Avoid recursion overhead.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def fib(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


# Alternate Python Solution: Top-Down Memoization
# - Uses recursion with caching.
# - Clear and intuitive.

from functools import lru_cache

class SolutionMemo:
    def fib(self, n: int) -> int:
        @lru_cache(None)
        def dfs(k):
            if k <= 1:
                return k
            return dfs(k - 1) + dfs(k - 2)
        return dfs(n)


# Additional Examples (Edge Cases and Non-LeetCode Examples)

sol = Solution()

# Example 1: Zero
print(sol.fib(0))
# Expected output: 0

# Example 2: One
print(sol.fib(1))
# Expected output: 1

# Example 3: Larger n
print(sol.fib(10))
# Expected output: 55

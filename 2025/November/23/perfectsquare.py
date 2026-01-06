# LeetCode 279: Perfect Squares
# Explanation:
# 1. We want the minimum number of perfect squares that sum to n.
# 2. Use dynamic programming (DP) where dp[i] = min number of squares summing to i.
# 3. Initialize dp[0] = 0.
# 4. For each number i from 1 to n:
#    - Try all squares j*j <= i.
#    - dp[i] = min(dp[i], dp[i - j*j] + 1)
# 5. dp[n] will give the answer.
# Time Complexity: O(n * sqrt(n)) because for each i we try sqrt(i) squares.
# Space Complexity: O(n) for the dp array.

from collections import deque

class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j*j] + 1)
                j += 1
        return dp[n]

    def numSquaresBFS(self, n: int) -> int:
        squares = [i*i for i in range(1, int(n**0.5)+1)]
        queue = deque([(n, 0)])
        visited = set()
        while queue:
            num, step = queue.popleft()
            if num == 0:
                return step
            for s in squares:
                if num - s >= 0 and num - s not in visited:
                    visited.add(num - s)
                    queue.append((num - s, step + 1))

    def numSquaresOneLine(self, n: int) -> int:
        dp = [0] + [min([dp[i - j*j] for j in range(1,int(i**0.5)+1)]) + 1 for i in range(1, n+1)]
        return dp[n]

print(Solution().numSquares(12))  # Output: 3 (4+4+4)
print(Solution().numSquares(13))  # Output: 2 (4+9)
print(Solution().numSquares(1))   # Output: 1 (1)
          

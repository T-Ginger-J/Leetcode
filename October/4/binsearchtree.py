# LeetCode 96: Unique Binary Search Trees
# Explanation:
# 1. The number of unique BSTs storing values 1..n is given by the nth Catalan number.
# 2. For each i in 1..n (root position):
#    - Left subtree has (i-1) nodes
#    - Right subtree has (n-i) nodes
#    - Total = G(i-1) * G(n-i)
# 3. Recurrence: G(n) = Σ G(i-1) * G(n-i), for i in [1..n]
# 4. Base: G(0) = 1, G(1) = 1
# Time Complexity: O(n^2)
# Space Complexity: O(n)

class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            for j in range(1, i + 1):
                dp[i] += dp[j - 1] * dp[i - j]
        return dp[n]

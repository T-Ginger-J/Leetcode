# LeetCode 441: Arranging Coins
# Explanation:
# You are given n coins and want to build a staircase where:
# - The 1st row has 1 coin
# - The 2nd row has 2 coins
# - ...
# - The k-th row has k coins
#
# The total number of coins needed to build k full rows is:
#   k * (k + 1) / 2
#
# We want to find the maximum k such that:
#   k * (k + 1) / 2 <= n
#
# Method 1: Mathematical Formula (Optimal)
# - Solve the quadratic inequality:
#     k^2 + k - 2n <= 0
# - Positive root:
#     k = floor((sqrt(1 + 8n) - 1) / 2)
#
# Time Complexity: O(1)
# Space Complexity: O(1)
#
# Method 2: Binary Search
# - Search for the largest k such that k*(k+1)/2 <= n
#
# Time Complexity: O(log n)
# Space Complexity: O(1)

import math

class Solution:
    # Method 1: Math (Optimal)
    def arrangeCoins(self, n: int) -> int:
        return int((math.isqrt(1 + 8 * n) - 1) // 2)

    # Method 2: Binary Search
    def arrangeCoinsBinarySearch(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid = (left + right) // 2
            coins = mid * (mid + 1) // 2
            if coins <= n:
                left = mid + 1
            else:
                right = mid - 1
        return right


# Additional Examples (Edge Cases and Non-LeetCode Examples)

# Example 1: No coins
print(Solution().arrangeCoins(0))   # Expected: 0

# Example 2: Exact triangular number
print(Solution().arrangeCoins(6))   # Expected: 3

# Example 3: Large n with leftover coins
print(Solution().arrangeCoins(8))   # Expected: 3

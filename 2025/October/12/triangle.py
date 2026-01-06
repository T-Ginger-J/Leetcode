# LeetCode 120: Triangle
# Explanation:
# 1. Given a triangle array, find the minimum path sum from top to bottom.
# 2. Each step you may move to adjacent numbers on the row below.
# 3. Use bottom-up DP:
#    - Start from the second last row.
#    - For each element, add the minimum of its two children below.
#    - The top element will end up as the min path sum.
# Time Complexity: O(n^2)
# Space Complexity: O(1) (in-place modification)

class Solution:
    def minimumTotal(self, triangle):
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1])
        return triangle[0][0]

    def minimumTotalDP(self, triangle):
        dp = triangle[-1][:]
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = triangle[i][j] + min(dp[j], dp[j + 1])
        return dp[0]
    
triangle = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
print(Solution().minimumTotal(triangle))
# Output: 11 (2 + 3 + 5 + 1)

triangle2 = [
    [-10]
]
print(Solution().minimumTotal(triangle2))
# Output: -10


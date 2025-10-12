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

# LeetCode 59: Spiral Matrix II
# Explanation:
# 1. Start with an n x n matrix of zeros.
# 2. Maintain four boundaries: top, bottom, left, right.
# 3. Fill numbers in spiral order while shrinking boundaries inward.
# Time Complexity: O(n^2)
# Space Complexity: O(1) extra (besides output matrix)

class Solution:
    def generateMatrix(self, n: int):
        matrix = [[0]*n for _ in range(n)]
        left, right, top, bottom = 0, n-1, 0, n-1
        num = 1
        
        while left <= right and top <= bottom:
            for i in range(left, right+1):
                matrix[top][i] = num
                num += 1
            top += 1
            
            for i in range(top, bottom+1):
                matrix[i][right] = num
                num += 1
            right -= 1
            
            if top <= bottom:
                for i in range(right, left-1, -1):
                    matrix[bottom][i] = num
                    num += 1
                bottom -= 1
            
            if left <= right:
                for i in range(bottom, top-1, -1):
                    matrix[i][left] = num
                    num += 1
                left += 1
        
        return matrix
    

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
    
    def generateMatrixOptimized(self, n: int):
        res = [[0]*n for _ in range(n)]
        num, layer = 1, 0
        while num <= n*n:
            for i in range(layer, n-layer):         # top row
                res[layer][i] = num
                num += 1
            for i in range(layer+1, n-layer):       # right col
                res[i][n-layer-1] = num
                num += 1
            if layer != n-layer-1:
                for i in range(n-layer-2, layer-1, -1):  # bottom row
                    res[n-layer-1][i] = num
                    num += 1
                for i in range(n-layer-2, layer, -1):    # left col
                    res[i][layer] = num
                    num += 1
            layer += 1
        return res
    
    generateMatrixOneLine = lambda n: __import__('numpy').rot90([list(range(i*n+1, i*n+n+1)) for i in range(n)], k=-1).tolist()

# Example usage:
# sol = Solution()
# print(sol.generateMatrix(3))
# print(sol.generateMatrix(1))

# LeetCode 498: Diagonal Traverse
# Explanation:
# Given an m x n matrix, return all elements in diagonal order.
# Diagonal order alternates between moving up-right and down-left.
#
# Method 1: Simulation
# - Use a loop to traverse diagonals using row+col = k.
# - Reverse elements of every other diagonal to get correct order.
#
# Time Complexity: O(m*n)
# Space Complexity: O(m*n)

from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        res = []
        for k in range(m + n - 1):
            intermediate = []
            for i in range(max(0, k - n + 1), min(m, k + 1)):
                j = k - i
                intermediate.append(mat[i][j])
            if k % 2 == 0:
                res.extend(intermediate[::-1])
            else:
                res.extend(intermediate)
        return res


# Alternate Python Solution: Direct Simulation with Direction Toggle
# - Keep track of current position and direction (up or down)
# - Move diagonally and handle boundary cases

class SolutionToggle:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        m, n = len(mat), len(mat[0])
        res = []
        i = j = 0
        up = True
        for _ in range(m * n):
            res.append(mat[i][j])
            if up:
                if j == n - 1:
                    i += 1
                    up = False
                elif i == 0:
                    j += 1
                    up = False
                else:
                    i -= 1
                    j += 1
            else:
                if i == m - 1:
                    j += 1
                    up = True
                elif j == 0:
                    i += 1
                    up = True
                else:
                    i += 1
                    j -= 1
        return res


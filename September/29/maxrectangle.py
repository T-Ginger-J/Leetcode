# LeetCode 85: Maximal Rectangle
# Explanation:
# 1. Treat each row as histogram of consecutive 1s.
# 2. For each row, compute largest rectangle in histogram using stack.
# 3. Track maximum rectangle area across rows.
# Time Complexity: O(m * n) where m=rows, n=cols
# Space Complexity: O(n)

class Solution:
    def maximalRectangle(self, matrix: list[list[str]]) -> int:
        if not matrix: return 0
        n = len(matrix[0])
        heights = [0] * (n + 1)  # extra 0 for flushing stack
        max_area = 0

        for row in matrix:
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0

            stack = []
            for i, h in enumerate(heights):
                while stack and heights[stack[-1]] > h:
                    height = heights[stack.pop()]
                    width = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, height * width)
                stack.append(i)
        return max_area

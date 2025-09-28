# LeetCode 84: Largest Rectangle in Histogram
# Explanation:
# 1. Use stack to store indices of increasing heights.
# 2. When a smaller bar is found, pop from stack and calculate area.
# 3. Continue until all bars processed.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        max_area = 0
        heights.append(0)  # sentinel to flush stack
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        heights.pop()
        return max_area

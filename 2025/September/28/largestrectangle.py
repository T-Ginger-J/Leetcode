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
    
    def largestRectangleAreaOptimized(self, heights: list[int]) -> int:
        n = len(heights)
        left, right = [-1]*n, [n]*n
        stack = []
        
        # nearest smaller to left
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        
        stack.clear()
        # nearest smaller to right
        for i in range(n-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = stack[-1] if stack else n
            stack.append(i)
        
        max_area = 0
        for i in range(n):
            max_area = max(max_area, heights[i] * (right[i] - left[i] - 1))
        return max_area
    
    largestRectangleAreaOneLine=lambda s,h:max((x:=sorted([(v,i)for i,v in enumerate(h+[0])]),[max(v*(i-(x[j-1][1] if j else -1)-1)for j,(v,i) in enumerate(x))])[1])

# Example usage:
# sol = Solution()
# print(sol.largestRectangleArea([2,1,5,6,2,3]))  # 10
# print(sol.largestRectangleArea([2,4]))          # 4

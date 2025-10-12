# LeetCode 119: Pascal’s Triangle II
# Explanation:
# 1. Return the kth (0-indexed) row of Pascal’s Triangle.
# 2. Each row can be computed iteratively using the previous one.
# 3. row[i] = prev[i - 1] + prev[i]
# Time Complexity: O(k^2)
# Space Complexity: O(k)

class Solution:
    def getRow(self, rowIndex: int):
        row = [1]
        for _ in range(rowIndex):
            row = [1] + [row[i] + row[i + 1] for i in range(len(row) - 1)] + [1]
        return row

    def getRowOneLine(self, k): return [math.comb(k, i) for i in range(k + 1)]

print(Solution().getRow(3))
# Output: [1, 3, 3, 1]

print(Solution().getRow(0))
# Output: [1]

print(Solution().getRow(5))
# Output: [1, 5, 10, 10, 5, 1]

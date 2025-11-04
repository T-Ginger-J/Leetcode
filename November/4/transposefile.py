# LeetCode 194: Transpose File (Python Equivalent)
# Explanation:
# 1. Read all lines and split by whitespace.
# 2. Use zip(*rows) to transpose the 2D list.
# Time Complexity: O(n * m)
# Space Complexity: O(n * m)

class Solution:
    def transposeFile(self, data: str):
        lines = [line.split() for line in data.strip().split('\n')]
        transposed = zip(*lines)
        return [' '.join(row) for row in transposed]

sol = Solution()
data = "name age\nalice 21\nryan 30"
print('\n'.join(sol.transposeFile(data)))
# Output:
# name alice ryan
# age 21 30

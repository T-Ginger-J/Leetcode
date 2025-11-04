# LeetCode 195: Tenth Line (Python Equivalent)
# Explanation:
# 1. Read all lines from file.
# 2. Print the 10th line if it exists.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def tenthLine(self, text: str):
        lines = text.strip().split('\n')
        return lines[9] if len(lines) >= 10 else ''

sol = Solution()
data = "\n".join([f"Line {i}" for i in range(1, 12)])
print(sol.tenthLine(data))  # Output: Line 10

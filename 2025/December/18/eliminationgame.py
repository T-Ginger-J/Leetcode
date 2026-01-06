# LeetCode 390: Elimination Game
# Explanation:
# 1. Track head, step, remaining, direction
# 2. Update head according to rules
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def lastRemaining(self, n: int) -> int:
        head = 1
        step = 1
        remaining = n
        left_to_right = True

        while remaining > 1:
            if left_to_right or remaining % 2 == 1:
                head += step
            remaining //= 2
            step *= 2
            left_to_right = not left_to_right

        return head

print(Solution().lastRemaining(9))   # Output: 6
print(Solution().lastRemaining(1))   # Output: 1
print(Solution().lastRemaining(10))  # Output: 8


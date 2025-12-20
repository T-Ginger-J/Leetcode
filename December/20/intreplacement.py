# LeetCode 397: Integer Replacement
# Explanation:
# 1. Divide by 2 if even
# 2. For odd, decide to increment or decrement based on last 2 bits
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def integerReplacement(self, n: int) -> int:
        steps = 0
        while n != 1:
            if n % 2 == 0:
                n //= 2
            else:
                if n == 3 or n % 4 == 1:
                    n -= 1
                else:
                    n += 1
            steps += 1
        return steps

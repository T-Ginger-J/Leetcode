# LeetCode 400: Nth Digit
# Explanation:
# 1. Group numbers by digit length
# 2. Locate exact number and digit position
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def findNthDigit(self, n: int) -> int:
        digits = 1
        count = 9
        start = 1

        while n > digits * count:
            n -= digits * count
            digits += 1
            count *= 10
            start *= 10

        # Find the exact number
        num = start + (n - 1) // digits
        num_str = str(num)
        return int(num_str[(n - 1) % digits])

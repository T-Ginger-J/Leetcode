# LeetCode 326: Power of Three
# Explanation:
# A number is a power of 3 if it can be divided by 3 repeatedly until it becomes 1.
# We handle n <= 0 as False.
#
# Time Complexity: O(log₃ n)
# Space Complexity: O(1)

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1

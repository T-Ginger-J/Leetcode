# LeetCode 172: Factorial Trailing Zeroes
# Explanation:
# 1. A trailing zero is formed by a pair of (2, 5) in factors.
# 2. Since there are more 2s than 5s, count how many 5s contribute.
# 3. Keep dividing n by 5 and add the quotient to the count.
# 4. Repeat until n becomes 0.
# Time Complexity: O(log₅n)
# Space Complexity: O(1)

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        while n > 0:
            n //= 5
            count += n
        return count


# LeetCode 357: Count Numbers with Unique Digits
# Explanation:
# 1. Use combinatorics for each number of digits.
# 2. Sum counts for all lengths 1..n.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        res = 10  # n = 1
        product = 9
        for i in range(2, n+1):
            product *= (11 - i)
            res += product
        return res

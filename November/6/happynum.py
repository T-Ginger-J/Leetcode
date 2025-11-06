# LeetCode 202: Happy Number
# Explanation:
# 1. Use a set to record previously seen numbers.
# 2. For each iteration, replace n with the sum of squares of digits.
# 3. If n == 1, return True; if n repeats, it's a cycle → return False.
# Time Complexity: O(log n)
# Space Complexity: O(log n)

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(d) ** 2 for d in str(n))
        return n == 1

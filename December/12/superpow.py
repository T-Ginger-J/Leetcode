# LeetCode 372: Super Pow
# Explanation:
# 1. Break b into digits, recursively compute modulo.
# 2. Use pow(a, k, mod) or helper to compute small powers.
# Time Complexity: O(log10(b) * log(a))
# Space Complexity: O(log10(b)) recursion

class Solution:
    MOD = 1337

    def superPow(self, a: int, b: list[int]) -> int:
        if not b:
            return 1
        last = b.pop()
        part1 = pow(a, last, self.MOD)
        part2 = pow(self.superPow(a, b), 10, self.MOD)
        return (part1 * part2) % self.MOD

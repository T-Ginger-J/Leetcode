import math

class Solution:
    # Method 1: Math (Optimal)
    def arrangeCoins(self, n: int) -> int:
        return int((math.isqrt(1 + 8 * n) - 1) // 2)


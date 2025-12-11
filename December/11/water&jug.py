# LeetCode 365: Water and Jug Problem
# Explanation:
# 1. Use gcd(x, y). Check if z % gcd == 0 and z <= x + y.
# Time Complexity: O(log(min(x, y)))
# Space Complexity: O(1)

import math

class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        if z > x + y:
            return False
        if z == 0 or z == x or z == y or z == x + y:
            return True
        return z % math.gcd(x, y) == 0

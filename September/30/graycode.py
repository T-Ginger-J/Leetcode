# LeetCode 89: Gray Code
# Explanation:
# 1. Gray code is a sequence where each successive number differs by only one bit.
# 2. The i-th gray code can be generated using formula: i ^ (i >> 1).
# 3. Generate gray codes from 0 to (2^n - 1).
# Time Complexity: O(2^n)
# Space Complexity: O(2^n)

from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        return [i ^ (i >> 1) for i in range(1 << n)]

# LeetCode 342: Power of Four
# Explanation:
# 1. Check n > 0
# 2. Check n is power of 2: n & (n - 1) == 0
# 3. Check its single '1' bit is in an even position:
#    n & 0x55555555 != 0
# Time Complexity: O(1)
# Space Complexity: O(1)

class Solution:
    def isPowerOfFour(self, n):
        return n > 0 and (n & (n - 1)) == 0 and (n & 0x55555555) != 0

# LeetCode 69: Sqrt(x)
# Explanation:
# 1. Use binary search between 0 and x.
# 2. Find largest mid such that mid^2 <= x.
# Time Complexity: O(log x)
# Space Complexity: O(1)

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 1, x // 2
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                left = mid + 1
            else:
                right = mid - 1
        return right

# LeetCode 367: Valid Perfect Square
# Explanation:
# 1. Use binary search from 1 to num.
# 2. Check if mid*mid == num.
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        left, right = 2, num // 2
        while left <= right:
            mid = (left + right) // 2
            sq = mid * mid
            if sq == num:
                return True
            elif sq < num:
                left = mid + 1
            else:
                right = mid - 1
        return False

print(Solution().isPerfectSquare(16))  # Output: True
print(Solution().isPerfectSquare(14))  # Output: False
print(Solution().isPerfectSquare(1))   # Output: True

# LeetCode 258: Add Digits
#
# Explanation:
# Repeatedly sum digits until the result is a single digit.
#
# Time Complexity: O(log n) per iteration, but overall small.
# Space Complexity: O(1)

class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            s = 0
            while num > 0:
                s += num % 10
                num //= 10
            num = s
        return num

# Example usage:
# sol = Solution()
# print(sol.addDigits(38))   # 2
# print(sol.addDigits(0))    # 0

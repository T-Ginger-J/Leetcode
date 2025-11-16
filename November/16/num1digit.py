# LeetCode 233: Number of Digit One
# Explanation:
# Count how many times '1' appears in each digit position (ones, tens, hundreds, ...)
#
# For each position factor (1, 10, 100, ...):
#   left  = n // (factor * 10)
#   digit = (n // factor) % 10
#   right = n % factor
#
# Contribution rules:
#   If digit == 0: left * factor
#   If digit == 1: left * factor + right + 1
#   If digit > 1:  (left + 1) * factor
#
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        factor = 1

        while factor <= n:
            left = n // (factor * 10)
            digit = (n // factor) % 10
            right = n % factor

            if digit == 0:
                count += left * factor
            elif digit == 1:
                count += left * factor + right + 1
            else:
                count += (left + 1) * factor

            factor *= 10

        return count

# Example usage:
sol = Solution()
print(sol.countDigitOne(13))  # 6  (1,10,11,12,13)
print(sol.countDigitOne(100)) # 21
print(sol.countDigitOne(20))   # 12
print(sol.countDigitOne(111))  # 36


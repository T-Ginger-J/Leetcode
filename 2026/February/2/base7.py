# LeetCode 504: Base 7
# Explanation:
# Given an integer num, return its base 7 representation as a string.
#
# Method 1: Repeated Division (Optimal)
# - Handle zero and negative numbers.
# - Repeatedly divide by 7 and record remainders.
# - Reverse the collected digits.
#
# Time Complexity: O(log_7 n)
# Space Complexity: O(log_7 n)

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        neg = num < 0
        num = abs(num)
        digits = []

        while num > 0:
            digits.append(str(num % 7))
            num //= 7

        res = "".join(reversed(digits))
        return "-" + res if neg else res


# Alternate Python Solution: Using Recursion
# - Recursively build the base-7 string.
# - Naturally handles digit order.

class SolutionRecursive:
    def convertToBase7(self, num: int) -> str:
        if num < 0:
            return "-" + self.convertToBase7(-num)
        if num < 7:
            return str(num)
        return self.convertToBase7(num // 7) + str(num % 7)


# Additional Examples (Edge Cases and Non-LeetCode Examples)

sol = Solution()

# Example 1: Zero
print(sol.convertToBase7(0))
# Expected output: "0"

# Example 2: Negative number
print(sol.convertToBase7(-49))
# Expected output: "-100"

# Example 3: Large number
print(sol.convertToBase7(343))
# Expected output: "1000"

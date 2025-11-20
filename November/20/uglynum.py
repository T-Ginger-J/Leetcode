# LeetCode 263: Ugly Number
#
# Explanation:
# A number is "ugly" if its prime factors are only 2,3,5.
# So repeatedly divide num by 2, 3, and 5 until no longer divisible.
# If final number becomes 1 → it's ugly.
#
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        for p in [2, 3, 5]:
            while num % p == 0:
                num //= p
        return num == 1

# Example usage:
# sol = Solution()
# print(sol.isUgly(6))  # True
# print(sol.isUgly(14)) # False

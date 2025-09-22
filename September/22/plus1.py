# LeetCode 66: Plus One
# Explanation:
# 1. Traverse from last digit backwards.
# 2. If digit < 9, increment and return.
# 3. If digit == 9, set to 0 and continue carry.
# 4. If all are 9's, prepend 1.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1] + digits
    plusOneOneLine=lambda s,d:[int(c) for c in str(int("".join(map(str,d)))+1)]

# Example usage:
# sol = Solution()
# print(sol.plusOne([1,2,3]))  # [1,2,4]
# print(sol.plusOne([9]))      # [1,0]

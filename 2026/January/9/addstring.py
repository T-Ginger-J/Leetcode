# LeetCode 415: Add Strings
# Explanation:
# 1. Start from end of both strings
# 2. Add digits with carry
# 3. Reverse result at the end
# Time Complexity: O(max(n, m))
# Space Complexity: O(max(n, m))

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        res = []
        while i >= 0 or j >= 0 or carry:
            x = int(num1[i]) if i >= 0 else 0
            y = int(num2[j]) if j >= 0 else 0
            total = x + y + carry
            res.append(str(total % 10))
            carry = total // 10
            i -= 1
            j -= 1
        return ''.join(res[::-1])

print(Solution().addStrings("11", "123"))   # Output: "134"
print(Solution().addStrings("456", "77"))   # Output: "533"
print(Solution().aaddStrings("0", "0"))      # Output: "0"

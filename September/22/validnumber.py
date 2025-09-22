# LeetCode 65: Valid Number
# Explanation:
# 1. Use a finite state machine or flags to track digit, exponent, decimal, and sign validity.
# 2. Iterate through string and validate each character.
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        num, dot, exp = False, False, False
        for i, ch in enumerate(s):
            if ch.isdigit():
                num = True
            elif ch in ['+', '-']:
                if i > 0 and s[i-1] not in ['e', 'E']:
                    return False
            elif ch == '.':
                if dot or exp:
                    return False
                dot = True
            elif ch in ['e', 'E']:
                if exp or not num:
                    return False
                exp, num = True, False
            else:
                return False
        return num

    def isNumberBuiltIn(self, s: str) -> bool:
        pattern = re.compile(r'^[+-]?((\d+(\.\d*)?)|(\.\d+))(e[+-]?\d+)?$', re.I)
        return bool(pattern.match(s.strip()))
# Example usage:
# sol = Solution()
# print(sol.isNumber("0"))      # True
# print(sol.isNumber("e"))      # False
# print(sol.isNumber("2e10"))   # True

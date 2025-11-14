# LeetCode 224: Basic Calculator
# Explanation:
# 1. Use a stack to store intermediate results.
# 2. Keep track of current number, result, and sign.
# 3. On '(' push current result and sign; on ')' pop and combine.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        res = 0
        sign = 1

        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in ['+', '-']:
                res += sign * num
                sign = 1 if c == '+' else -1
                num = 0
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ')':
                res += sign * num
                num = 0
                res *= stack.pop()  # sign
                res += stack.pop()  # previous result
        return res + sign * num
    

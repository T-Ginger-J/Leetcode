# LeetCode 227: Basic Calculator II
# Explanation:
# 1. Use a single-pass parser with a stack to handle operator precedence.
#    - Keep current number (num) and last seen operator (op).
#    - When we see an operator (or reach end), apply the previous operator:
#        '+' -> push num
#        '-' -> push -num
#        '*' -> pop last, push last * num
#        '/' -> pop last, push int(last / num) (truncate toward zero)
# 2. At the end sum the stack to get result.
#
# Time Complexity: O(n) where n = length of string (single pass).
# Space Complexity: O(n) in worst case for the stack (but usually less).

class Solution:
    def calculate(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        stack = []
        num = 0
        op = '+'  # pretend there's a '+' before the expression
        i = 0
        while i < len(s):
            ch = s[i]
            if ch.isdigit():
                num = num * 10 + int(ch)
            if (not ch.isdigit() and ch != ' ') or i == len(s) - 1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    last = stack.pop()
                    stack.append(last * num)
                elif op == '/':
                    last = stack.pop()
                    # Python truncates toward -inf for negative numbers; we need truncate toward 0
                    stack.append(int(last / num))
                op = ch
                num = 0
            i += 1
        return sum(stack)

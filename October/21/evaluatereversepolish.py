# LeetCode 150: Evaluate Reverse Polish Notation
# Explanation:
# 1. Use a stack to evaluate postfix expressions.
# 2. Traverse tokens: push numbers to stack, pop two for operations.
# 3. Perform arithmetic and push result back to stack.
# 4. Return top of stack as final result.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def evalRPN(self, tokens):
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                b, a = stack.pop(), stack.pop()
                if t == '+': stack.append(a + b)
                elif t == '-': stack.append(a - b)
                elif t == '*': stack.append(a * b)
                else: stack.append(int(a / b))  # Truncate toward 0
        return stack[0]


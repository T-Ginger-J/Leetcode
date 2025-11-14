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

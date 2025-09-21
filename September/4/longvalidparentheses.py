#O(n)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]  # base index
        max_len = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len = max(max_len, i - stack[-1])

        return max_len
    
    def longestValidParenthesesDP(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0

        dp = [0] * n
        max_len = 0

        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = (dp[i-2] if i >= 2 else 0) + 2
                elif i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(':
                    dp[i] = dp[i-1] + 2 + (dp[i - dp[i-1] - 2] if i - dp[i-1] >= 2 else 0)
                max_len = max(max_len, dp[i])

        return max_len


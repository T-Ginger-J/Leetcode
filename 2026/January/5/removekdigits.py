# LeetCode 402: Remove K Digits
# Explanation:
# 1. Use stack to maintain increasing digits
# 2. Pop digits if current digit is smaller and k > 0
# 3. Remove leading zeros
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
            stack.append(digit)
        # Remove remaining digits from the end
        while k > 0:
            stack.pop()
            k -= 1
        # Build number and remove leading zeros
        result = ''.join(stack).lstrip('0')
        return result if result else "0"

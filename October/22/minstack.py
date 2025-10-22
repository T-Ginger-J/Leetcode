# LeetCode 155: Min Stack
# Explanation:
# 1. Use two stacks: one for all values (stack) and one for current minimums (min_stack).
# 2. When pushing, also push the new min if it’s smaller or equal to the top of min_stack.
# 3. When popping, if the popped value equals min_stack’s top, pop from both.
# 4. getMin() always returns the top of min_stack in O(1).
# Time Complexity: O(1) per operation
# Space Complexity: O(n)

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.min_stack[-1]:
            self.min_stack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

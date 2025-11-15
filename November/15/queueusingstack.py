# LeetCode 232: Implement Queue Using Stacks
# Explanation:
# Use two stacks:
# - in_stack for pushing elements
# - out_stack for popping/front operations
#
# When popping/front:
#   If out_stack is empty, move all items from in_stack → out_stack.
#
# Time Complexity:
#   - Push: O(1)
#   - Pop: Amortized O(1)
#   - Peek: Amortized O(1)
#   - Empty: O(1)
#
# Space Complexity: O(n)

class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._shift()
        return self.out_stack.pop()

    def peek(self) -> int:
        self._shift()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

    def _shift(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

# LeetCode 225: Implement Stack using Queues
# Explanation:
# 1. Use a single queue (collections.deque).
# 2. On push: enqueue and then rotate the queue so the new element is at the front.
# 3. pop() and top() both operate on the left side (front).
# Time Complexity: O(n) for push, O(1) for pop/top.
# Space Complexity: O(n)

from collections import deque

class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return not self.q

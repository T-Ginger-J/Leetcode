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
    
class MyStackTwoQueue:
    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return not self.q1


s = MyStack()
s.push(1)
s.push(2)
print(s.top())   # 2
print(s.pop())   # 2
print(s.empty()) # False

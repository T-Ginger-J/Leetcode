# LeetCode 284: Peeking Iterator
# Explanation:
# 1. The iterator is provided as a LeetCode Iterator class object.
# 2. We store the next element in a cache variable.
# 3. peek() returns the cached value without advancing.
# 4. next() returns the cached value and moves the iterator forward.
# 5. hasNext() checks if the cached value exists.
# Time Complexity: O(1) per operation
# Space Complexity: O(1)

class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self._next = iterator.next() if iterator.hasNext() else None

    def peek(self):
        return self._next

    def next(self):
        current = self._next
        self._next = self.iterator.next() if self.iterator.hasNext() else None
        return current

    def hasNext(self):
        return self._next is not None

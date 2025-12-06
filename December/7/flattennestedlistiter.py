class NestedIterator:
    def __init__(self, nestedList):
        self.stack = nestedList[::-1]

    def next(self):
        return self.stack.pop()

    def hasNext(self):
        while self.stack and not self.stack[-1].isInteger():
            lst = self.stack.pop().getList()
            for x in reversed(lst):
                self.stack.append(x)
        return bool(self.stack)

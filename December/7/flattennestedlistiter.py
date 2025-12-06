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

class NestedIteratorInit:
    def __init__(self, nestedList):
        self.flat = []
        self.index = 0

        def dfs(lst):
            for x in lst:
                if x.isInteger():
                    self.flat.append(x.getInteger())
                else:
                    dfs(x.getList())

        dfs(nestedList)

    def next(self):
        val = self.flat[self.index]
        self.index += 1
        return val

    def hasNext(self):
        return self.index < len(self.flat)

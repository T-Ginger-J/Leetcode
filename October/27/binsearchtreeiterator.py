class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self._push_left(root)
    
    def _push_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self):
        node = self.stack.pop()
        val = node.val
        if node.right:
            self._push_left(node.right)
        return val

    def hasNext(self):
        return len(self.stack) > 0

from typing import List
import random
import bisect

class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.weights = []
        total = 0
        for x1, y1, x2, y2 in rects:
            cnt = (x2 - x1 + 1) * (y2 - y1 + 1)
            total += cnt
            self.weights.append(total)

    def pick(self) -> List[int]:
        r = random.randint(1, self.weights[-1])
        idx = bisect.bisect_left(self.weights, r)
        x1, y1, x2, y2 = self.rects[idx]
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)
        return [x, y]


import random

class Solution:
    def __init__(self, nums):
        self.original = list(nums)

    def reset(self):
        return list(self.original)

    def shuffle(self):
        shuffled = list(self.original)
        n = len(shuffled)
        for i in range(n-1, 0, -1):
            j = random.randint(0, i)
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        return shuffled

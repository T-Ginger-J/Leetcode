
import random
import math

class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.R = radius
        self.xc = x_center
        self.yc = y_center

    def randPoint(self):
        theta = random.random() * 2 * math.pi
        r = self.R * math.sqrt(random.random())
        x = self.xc + r * math.cos(theta)
        y = self.yc + r * math.sin(theta)
        return [x, y]

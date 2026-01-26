# LeetCode 478: Generate Random Point in a Circle
# Explanation:
# Given the radius and center of a circle, generate a random point uniformly
# inside the circle.
#
# Method 1: Polar Coordinates (Optimal)
# - Uniform angle: theta ∈ [0, 2π)
# - Uniform radius requires sqrt(rand) scaling:
#     r = R * sqrt(u), where u ∈ [0,1)
# - Convert to Cartesian:
#     x = x_center + r * cos(theta)
#     y = y_center + r * sin(theta)
#
# Time Complexity: O(1) per call
# Space Complexity: O(1)

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


# Alternate Python Solution: Rejection Sampling
# - Sample uniformly in the bounding square.
# - Reject points outside the circle.
#
# Time Complexity: Expected O(1)
# Space Complexity: O(1)

class SolutionRejection:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self.R = radius
        self.xc = x_center
        self.yc = y_center

    def randPoint(self):
        while True:
            x = random.uniform(-self.R, self.R)
            y = random.uniform(-self.R, self.R)
            if x * x + y * y <= self.R * self.R:
                return [self.xc + x, self.yc + y]


# Additional Examples (Non-LeetCode, Edge-Oriented)

sol = Solution(1.0, 0.0, 0.0)

# Example 1: Single call inside unit circle
p = sol.randPoint()
print(p[0] * p[0] + p[1] * p[1] <= 1.0)
# Expected output: True

# Example 2: Shifted center
sol2 = Solution(2.0, 5.0, -3.0)
p2 = sol2.randPoint()
print((p2[0] - 5.0)**2 + (p2[1] + 3.0)**2 <= 4.0)
# Expected output: True

# Example 3: Multiple samples bounds check
pts = [sol.randPoint() for _ in range(1000)]
print(all(x*x + y*y <= 1.0 for x, y in pts))
# Expected output: True

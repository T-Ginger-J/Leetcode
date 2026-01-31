# LeetCode 495: Teemo Attacking
# Explanation:
# Teemo attacks Ashe, dealing poison for a duration. Overlapping attacks
# extend the poison, but do not stack. Return total poisoned time.
#
# Method 1: Linear Scan (Optimal)
# - Iterate through attacks.
# - For each attack, add min(duration, time to next attack) to total.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0
        total = 0
        for i in range(len(timeSeries) - 1):
            total += min(duration, timeSeries[i+1] - timeSeries[i])
        total += duration  # last attack
        return total


from typing import List


class Solution:

    # -------------------------------------------------------
    # Method 1: Sorting + Consecutive Difference
    # -------------------------------------------------------
    def findMinDifference(self, timePoints: List[str]) -> int:

        minutes = []

        for t in timePoints:
            h, m = map(int, t.split(':'))
            minutes.append(h * 60 + m)

        minutes.sort()
        min_diff = float('inf')
        n = len(minutes)

        for i in range(1, n):
            min_diff = min(min_diff, minutes[i] - minutes[i-1])

        # circular difference
        min_diff = min(min_diff, 1440 - (minutes[-1] - minutes[0]))

        return min_diff



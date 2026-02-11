# LeetCode 539: Minimum Time Difference
# Explanation:
# 1. Given a list of 24-hour time points (HH:MM), find the minimum difference in minutes between any two.
# 2. Convert times to minutes, sort, and compare consecutive times including circular difference across midnight.

# Methods Used:
# - Convert to minutes
# - Sort and compare consecutive differences
# - Handle wrap-around (last and first)

# Time Complexity:
# - O(n log n), n = number of time points

# Space Complexity:
# - O(n) for minutes list


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


# -------------------------------------------------------
# Examples (Including Edge Cases)
# -------------------------------------------------------

# Example 1
timePoints1 = ["23:59","00:00"]
print(Solution().findMinDifference(timePoints1))  # 1

# Example 2
timePoints2 = ["00:00","23:59","12:30"]
print(Solution().findMinDifference(timePoints2))  # 1

# Example 3 (Multiple same times)
timePoints3 = ["01:01","01:01","02:01"]
print(Solution().findMinDifference(timePoints3))  # 0

# Example 4 (Single minute difference)
timePoints4 = ["05:31","22:08","00:35"]
print(Solution().findMinDifference(timePoints4))  # 147 (min between 22:08 and 00:35)

# Example 5 (Wrap-around case)
timePoints5 = ["23:59","00:01","12:00"]
print(Solution().findMinDifference(timePoints5))  # 2

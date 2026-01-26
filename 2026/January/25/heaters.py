# LeetCode 475: Heaters
# Explanation:
# Given positions of houses and heaters on a line, find the minimum radius
# required so that every house is within range of at least one heater.
#
# Method 1: Binary Search on Heaters (Optimal)
# - Sort both houses and heaters.
# - For each house, find the nearest heater using binary search.
# - Track the maximum distance needed across all houses.
#
# Time Complexity: O(n log m)
# Space Complexity: O(1) extra (excluding sorting)

from typing import List
import bisect

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        radius = 0
        for house in houses:
            idx = bisect.bisect_left(heaters, house)

            left_dist = float('inf')
            right_dist = float('inf')

            if idx > 0:
                left_dist = house - heaters[idx - 1]
            if idx < len(heaters):
                right_dist = heaters[idx] - house

            radius = max(radius, min(left_dist, right_dist))

        return radius


# Alternate Python Solution: Two Pointers
# - Walk through houses while tracking nearest heater.
# - Avoids binary search per house.
#
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1)

class SolutionTwoPointers:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        i = 0
        res = 0
        for house in houses:
            while i + 1 < len(heaters) and abs(heaters[i + 1] - house) <= abs(heaters[i] - house):
                i += 1
            res = max(res, abs(heaters[i] - house))
        return res


# Additional Examples (Edge Cases and Non-LeetCode Examples)

sol = Solution()

# Example 1: Single heater covers all
print(sol.findRadius([1, 2, 3], [2]))
# Expected output: 1

# Example 2: Heater on one side only
print(sol.findRadius([1, 5], [10]))
# Expected output: 9

# Example 3: Houses and heaters overlap
print(sol.findRadius([1, 2, 3, 4], [1, 4]))
# Expected output: 1

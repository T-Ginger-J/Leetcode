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


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


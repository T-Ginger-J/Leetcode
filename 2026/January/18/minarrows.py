# LeetCode 452: Minimum Number of Arrows to Burst Balloons
# Explanation:
# Each balloon is represented as an interval [start, end].
# An arrow shot at position x bursts all balloons where start <= x <= end.
# Goal: find the minimum number of arrows to burst all balloons.
#
# Method 1: Greedy by End Coordinate (Optimal)
# - Sort balloons by their end coordinate.
# - Shoot the first arrow at the end of the first balloon.
# - For each next balloon:
#     - If its start > current arrow position, we need a new arrow.
#     - Otherwise, it is already burst by the current arrow.
#
# This is equivalent to interval scheduling / minimum points to cover intervals.
#
# Time Complexity: O(n log n)
# Space Complexity: O(1) (sorting aside)

from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])
        arrows = 1
        curr_end = points[0][1]

        for start, end in points[1:]:
            if start > curr_end:
                arrows += 1
                curr_end = end

        return arrows


# Additional Examples (Edge Cases and Non-LeetCode Examples)

sol = Solution()

# Example 1: Overlapping intervals
points1 = [[10,16],[2,8],[1,6],[7,12]]
print(sol.findMinArrowShots(points1))
# Expected output: 2

# Example 2: No overlaps
points2 = [[1,2],[3,4],[5,6]]
print(sol.findMinArrowShots(points2))
# Expected output: 3

# Example 3: All balloons overlap at one point
points3 = [[1,10],[2,9],[3,8],[4,7]]
print(sol.findMinArrowShots(points3))
# Expected output: 1

# LeetCode 447: Number of Boomerangs
# Explanation:
# Given n points in the plane, a "boomerang" is a tuple (i, j, k)
# such that distance(i, j) == distance(i, k) and i, j, k are distinct.
# Goal: count all boomerangs.
#
# Method 1: Hashmap Counting (Optimal)
# - For each point i:
#     1. Compute distances to all other points j.
#     2. Use a hashmap to count how many points are at each distance.
#     3. For each distance with count c, it contributes c * (c - 1) boomerangs
#        (permutations of j and k)
#
# Time Complexity: O(n^2)
# Space Complexity: O(n) (for hashmap per point)

from typing import List
from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for i in points:
            dist_count = defaultdict(int)
            for j in points:
                if i == j:
                    continue
                dx = i[0] - j[0]
                dy = i[1] - j[1]
                dist = dx*dx + dy*dy
                dist_count[dist] += 1
            for count in dist_count.values():
                res += count * (count - 1)
        return res

# Additional Examples (Edge Cases and Non-LeetCode Examples)

sol = Solution()

# Example 1: Simple square
points1 = [[0,0],[1,0],[2,0]]
print(sol.numberOfBoomerangs(points1))  
# Expected output: 2
# (Boomerangs: (1,0,2) and (1,2,0))

# Example 2: All points at same distance
points2 = [[0,0],[1,0],[0,1],[1,1]]
print(sol.numberOfBoomerangs(points2))  
# Expected output: 8

# Example 3: Only one point
points3 = [[0,0]]
print(sol.numberOfBoomerangs(points3))  
# Expected output: 0

# LeetCode 335: Self Crossing
# Explanation:
# Given distances for movements in order:
#   north, west, south, east, north, west, ...
#
# We detect if the path crosses itself.
#
# Key Insight:
# A self-crossing can happen in 3 cases:
#
# Case 1 (current crosses 3 steps back):
#   i >= 3 and x[i] >= x[i-2] and x[i-1] <= x[i-3]
#
# Case 2 (current meets line 4 steps back):
#   i >= 4 and x[i-1] == x[i-3] and x[i] + x[i-4] >= x[i-2]
#
# Case 3 (current crosses 5 steps back):
#   i >= 5 and:
#       x[i-2] >= x[i-4] and
#       x[i] + x[i-4] >= x[i-2] and
#       x[i-1] <= x[i-3] and
#       x[i-1] + x[i-5] >= x[i-3]
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def isSelfCrossing(self, x):
        for i in range(3, len(x)):

            # Case 1: crosses 3 steps back
            if x[i] >= x[i-2] and x[i-1] <= x[i-3]:
                return True

            # Case 2: meets line 4 steps back
            if i >= 4 and x[i-1] == x[i-3] and x[i] + x[i-4] >= x[i-2]:
                return True

            # Case 3: crosses 5 steps back
            if i >= 5:
                if (
                    x[i-2] >= x[i-4] and
                    x[i] + x[i-4] >= x[i-2] and
                    x[i-1] <= x[i-3] and
                    x[i-1] + x[i-5] >= x[i-3]
                ):
                    return True

        return False

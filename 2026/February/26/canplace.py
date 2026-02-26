# LeetCode 605: Can Place Flowers
# Explanation:
# 1. Given a flowerbed array (0 = empty, 1 = planted), and n flowers to plant.
# 2. Rule: flowers cannot be planted in adjacent plots.
# 3. Approach:
#    - Iterate over the array.
#    - If current plot is 0 and neighbors (previous and next) are 0 or boundary, plant a flower.
#    - Decrement n each time we plant.
#    - Early exit if n <= 0.
# 4. Time Complexity: O(len(flowerbed))
# 5. Space Complexity: O(1)

from typing import List

class Solution:

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length = len(flowerbed)
        for i in range(length):
            if flowerbed[i] == 0:
                empty_prev = (i == 0) or (flowerbed[i-1] == 0)
                empty_next = (i == length-1) or (flowerbed[i+1] == 0)
                if empty_prev and empty_next:
                    flowerbed[i] = 1
                    n -= 1
                    if n <= 0:
                        return True
        return n <= 0


# -------------------------------------------------------
# Examples & Edge Cases
# -------------------------------------------------------

sol = Solution()

# Example 1
print(sol.canPlaceFlowers([1,0,0,0,1], 1))  # True

# Example 2
print(sol.canPlaceFlowers([1,0,0,0,1], 2))  # False

# Example 3: Empty flowerbed
print(sol.canPlaceFlowers([0,0,0,0,0], 3))  # True

# Example 4: Single plot
print(sol.canPlaceFlowers([0], 1))  # True

# Example 5: Single plot occupied
print(sol.canPlaceFlowers([1], 1))  # False

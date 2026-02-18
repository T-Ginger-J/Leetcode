# LeetCode 575: Distribute Candies
# Explanation:
# 1. Given an integer array candies representing different kinds of candies, distribute them equally to a brother and sister.
# 2. Task: Return the maximum number of unique candy kinds the sister could get.
# 3. Approach:
#    - Sister gets half of the total candies.
#    - Maximum unique kinds she can get = min(number of unique candies, total_candies // 2)
# 4. Time Complexity: O(n)
# 5. Space Complexity: O(n) for set of unique candies

from typing import List

class Solution:

    # -------------------------------------------------------
    # Method 1: Using set
    # -------------------------------------------------------
    def distributeCandies(self, candies: List[int]) -> int:
        unique_candies = len(set(candies))
        return min(unique_candies, len(candies)//2)

    # -------------------------------------------------------
    # Method 2: Using dictionary counter
    # -------------------------------------------------------
    def distributeCandiesCounter(self, candies: List[int]) -> int:
        from collections import Counter
        counter = Counter(candies)
        return min(len(counter), len(candies)//2)


from typing import List

class Solution:

    # -------------------------------------------------------
    # Method 1: Using set
    # -------------------------------------------------------
    def distributeCandies(self, candies: List[int]) -> int:
        unique_candies = len(set(candies))
        return min(unique_candies, len(candies)//2)

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


# -------------------------------------------------------
# Examples & Edge Cases
# -------------------------------------------------------

sol = Solution()

# Example 1
candies1 = [1,1,2,2,3,3]
print(sol.distributeCandies(candies1))          # 3
print(sol.distributeCandiesCounter(candies1))   # 3

# Example 2: all same
candies2 = [1,1,1,1]
print(sol.distributeCandies(candies2))          # 1

# Example 3: all unique
candies3 = [1,2,3,4]
print(sol.distributeCandies(candies3))          # 2 (half total)

# Example 4: one candy
candies4 = [5]
print(sol.distributeCandies(candies4))          # 1

# Example 5: empty list
candies5 = []
print(sol.distributeCandies(candies5))          # 0

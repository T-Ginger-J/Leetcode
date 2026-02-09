# LeetCode 528: Random Pick with Weight
# Explanation:
# 1. We are given a list of positive weights w.
# 2. We need to pick an index randomly, where the probability of each index
#    is proportional to its weight.
# 3. Use prefix sum and binary search to achieve weighted random pick.

# Methods Used:
# - Prefix Sum Array + Binary Search
# - Random Selection within Total Weight

# Time Complexity:
# - Initialization: O(n)
# - pickIndex(): O(log n)

# Space Complexity:
# - O(n) for prefix sum array


from typing import List
import random
import bisect


class Solution:

    # -------------------------------------------------------
    # Method 1: Prefix Sum + Binary Search (Optimal)
    # -------------------------------------------------------
    def __init__(self, w: List[int]):
        self.prefix = []
        total = 0
        for weight in w:
            total += weight
            self.prefix.append(total)
        self.total = total

    def pickIndex(self) -> int:
        target = random.randint(1, self.total)
        # Binary search for the first prefix >= target
        idx = bisect.bisect_left(self.prefix, target)
        return idx


# -------------------------------------------------------
# Examples (Including Edge Cases)
# -------------------------------------------------------

# Example 1
w = [1, 3]
obj = Solution(w)
# Probabilities: index 0 -> 1/4, index 1 -> 3/4
results = [obj.pickIndex() for _ in range(10000)]
# Check approximate di

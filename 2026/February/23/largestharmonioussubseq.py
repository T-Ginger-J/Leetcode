# LeetCode 594: Longest Harmonious Subsequence
# Explanation:
# 1. A harmonious subsequence is one where:
#    max(subsequence) - min(subsequence) == 1
# 2. We need the longest such subsequence.
# 3. Order does not matter (subsequence, not substring).
# 4. Approach:
#    - Count frequency of each number.
#    - For each number x, check if x+1 exists.
#    - If yes, candidate length = freq[x] + freq[x+1].
# 5. Take the maximum over all x.
# 6. Time Complexity: O(n)
# 7. Space Complexity: O(n)

from typing import List
from collections import Counter


class Solution:

    def findLHS(self, nums: List[int]) -> int:

        freq = Counter(nums)

        ans = 0

        for x in freq:
            if x + 1 in freq:
                ans = max(ans, freq[x] + freq[x + 1])

        return ans


# -------------------------------------------------------
# Examples & Edge Cases
# -------------------------------------------------------

sol = Solution()

# Example 1
print(sol.findLHS([1,3,2,2,5,2,3,7]))   # 5  (2,2,2,3,3)

# Example 2
print(sol.findLHS([1,2,3,4]))          # 2

# Example 3
print(sol.findLHS([1,1,1,1]))          # 0

# Example 4: Negative numbers
print(sol.findLHS([-1,-2,-3,-2,-1]))   # 4  (-2,-2,-1,-1)

# Example 5: Single element
print(sol.findLHS([10]))              # 0

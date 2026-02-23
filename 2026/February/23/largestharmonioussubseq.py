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


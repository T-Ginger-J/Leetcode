# LeetCode 209: Minimum Size Subarray Sum
# Explanation:
# 1. Use two pointers (start, end) to maintain a sliding window.
# 2. Expand end to increase sum, contract start to minimize length.
# 3. Track minimal window where sum >= target.
# Time Complexity: O(n)
# Space Complexity: O(1)

import bisect

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        prefix = [0]
        for n in nums:
            prefix.append(prefix[-1] + n)
        res = float('inf')
        for i in range(len(nums)):
            desired = prefix[i] + target
            j = bisect.bisect_left(prefix, desired)
            if j < len(prefix):
                res = min(res, j - i)
        return 0 if res == float('inf') else res

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

    def minSubArrayLenSlidingWindow(self, target: int, nums: list[int]) -> int:
        left = 0
        total = 0
        min_len = float('inf')

        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                min_len = min(min_len, right - left + 1)
                total -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len


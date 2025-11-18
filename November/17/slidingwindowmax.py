# LeetCode 239: Sliding Window Maximum
# Explanation:
# Use a deque that stores indices in decreasing order of values.
# Steps:
# 1. Pop from back while current number is larger → maintain decreasing order.
# 2. Push current index.
# 3. Remove front if it's outside the window.
# 4. The front of the deque is always the max for the window.
#
# Time Complexity: O(n)
# Space Complexity: O(k)

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        dq = deque()
        res = []

        for i, num in enumerate(nums):
            # Remove smaller values from back
            while dq and nums[dq[-1]] <= num:
                dq.pop()

            dq.append(i)

            # Remove out-of-window index
            if dq[0] == i - k:
                dq.popleft()

            # Add max to result once window is valid
            if i >= k - 1:
                res.append(nums[dq[0]])

        return res

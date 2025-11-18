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

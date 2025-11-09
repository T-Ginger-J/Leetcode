
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

from bisect import bisect_left, insort, bisect_right

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        window = []
        for i, n in enumerate(nums):
            pos = bisect_left(window, n)
            if pos < len(window) and abs(window[pos] - n) <= valueDiff:
                return True
            if pos > 0 and abs(window[pos-1] - n) <= valueDiff:
                return True

            insort(window, n)
            if len(window) > indexDiff:
                del window[bisect_left(window, nums[i - indexDiff])]
        return False

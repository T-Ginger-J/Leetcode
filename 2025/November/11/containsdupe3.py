# LeetCode 220: Contains Duplicate III
# Explanation:
# 1. Divide numbers into "buckets" of width = valueDiff + 1.
# 2. If two numbers fall in the same bucket, abs(diff) <= valueDiff.
# 3. Check neighboring buckets (adjacent values may be close).
# 4. Maintain window of size <= indexDiff.
# Time Complexity: O(n)
# Space Complexity: O(n)

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

sol = Solution()
print(sol.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0))      # True
print(sol.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3))  # False
print(sol.containsNearbyAlmostDuplicate([1,2,3,1], 3, 1))      # True

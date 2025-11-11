# LeetCode 219: Contains Duplicate II
# Explanation:
# 1. Use a dictionary to store the last seen index of each number.
# 2. If the number is seen again and |i - prev_i| <= k, return True.
# 3. Otherwise, update index in dictionary.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = {}
        for i, n in enumerate(nums):
            if n in seen and i - seen[n] <= k:
                return True
            seen[n] = i
        return False

    def containsNearbyDuplicateSlidingWindow(self, nums: list[int], k: int) -> bool:
        window = set()
        for i, n in enumerate(nums):
            if n in window:
                return True
            window.add(n)
            if len(window) > k:
                window.remove(nums[i - k])
        return False

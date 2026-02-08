# LeetCode 532: K-diff Pairs in an Array
# Explanation:
# 1. Given an integer array nums and integer k, find the number of unique k-diff pairs.
#    A k-diff pair is (nums[i], nums[j]) where i != j and |nums[i]-nums[j]| == k.
# 2. Use a hashmap or set to track numbers and count pairs.

# Methods Used:
# - Hash Map Counting
# - Set for Unique Pairs
# - Sorting + Two Pointers Alternative

# Time Complexity:
# - O(n) for hashmap method
# - O(n log n) for sorting + two pointers

# Space Complexity:
# - O(n) for hashmap or set


from typing import List
from collections import Counter


class Solution:

    # -------------------------------------------------------
    # Method 1: Hash Map Counting (Optimal)
    # -------------------------------------------------------
    def findPairs(self, nums: List[int], k: int) -> int:

        if k < 0:
            return 0  # absolute difference can't be negative

        count = 0
        freq = Counter(nums)

        if k == 0:
            # Count numbers appearing at least twice
            for val in freq.values():
                if val >= 2:
                    count += 1
        else:
            # Count unique nums where num+k exists
            for num in freq:
                if num + k in freq:
                    count += 1

        return count

    # -------------------------------------------------------
    # Method 2: Sorting + Two Pointers
    # -------------------------------------------------------
    def findPairsTwoPointers(self, nums: List[int], k: int) -> int:

        if k < 0:
            return 0

        nums.sort()
        n = len(nums)
        count = 0
        i, j = 0, 1

        while i < n and j < n:
            if i == j or nums[j] - nums[i] < k:
                j += 1
            elif nums[j] - nums[i] > k:
                i += 1
            else:
                count += 1
                i += 1
                j += 1
                while j < n and nums[j] == nums[j - 1]:
                    j += 1
                while i < n and nums[i] == nums[i - 1]:
                    i += 1

        return count


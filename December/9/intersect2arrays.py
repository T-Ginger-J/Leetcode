# LeetCode 349: Intersection of Two Arrays
# Explanation:
# 1. Convert both arrays to sets to remove duplicates.
# 2. Return the intersection as a list.
# Time Complexity: O(n + m)
# Space Complexity: O(n + m)

class Solution:
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))

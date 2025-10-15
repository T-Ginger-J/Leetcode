# LeetCode 128: Longest Consecutive Sequence
# Explanation:
# 1. Use a set for O(1) lookups.
# 2. For each number, check if it’s the start of a sequence (num - 1 not in set).
# 3. Count the consecutive numbers and update the max length.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0
        
        for num in num_set:
            if num - 1 not in num_set:  # start of a sequence
                length = 1
                while num + length in num_set:
                    length += 1
                longest = max(longest, length)
        return longest

# LeetCode 169: Majority Element
# Explanation:
# 1. The majority element appears more than ⌊n/2⌋ times.
# 2. Count occurrences of each element using a hashmap.
# 3. Return the element whose count > n/2.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def majorityElement(self, nums):
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
            if counts[n] > len(nums) // 2:
                return n


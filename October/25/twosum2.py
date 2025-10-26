# LeetCode 167: Two Sum II – Input Array Is Sorted
# Explanation:
# 1. Use two pointers: one at start (left), one at end (right).
# 2. Compute sum = numbers[left] + numbers[right].
# 3. If sum == target → return [left+1, right+1].
# 4. If sum < target → move left pointer up (increase sum).
# 5. If sum > target → move right pointer down (decrease sum).
# Time Complexity: O(n)
# Space Complexity: O(1)


import bisect

class Solution:
    def twoSum(self, numbers, target):
        left, right = 0, len(numbers) - 1
        while left < right:
            s = numbers[left] + numbers[right]
            if s == target:
                return [left + 1, right + 1]
            elif s < target:
                left += 1
            else:
                right -= 1

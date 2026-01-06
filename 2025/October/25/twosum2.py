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

    def twoSumBinSearch(self, numbers, target):
        for i, n in enumerate(numbers):
            complement = target - n
            j = bisect.bisect_left(numbers, complement, i + 1)
            if j < len(numbers) and numbers[j] == complement:
                return [i + 1, j + 1]
            
print(Solution().twoSum([2,7,11,15], 9))
# Output: [1, 2]

print(Solution().twoSum([2,3,4], 6))
# Output: [1, 3]

print(Solution().twoSum([-1,0], -1))
# Output: [1, 2]

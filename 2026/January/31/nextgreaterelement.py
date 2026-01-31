# LeetCode 496: Next Greater Element I
# Explanation:
# Given two arrays nums1 and nums2, find the next greater element of each
# element in nums1 within nums2.
#
# Method 1: Monotonic Stack + Hash Map (Optimal)
# - Iterate nums2 and use a stack to keep track of decreasing elements.
# - When a larger element appears, pop from stack and record next greater.
# - Lookup for nums1 in the hashmap for results.
#
# Time Complexity: O(n + m), n = len(nums1), m = len(nums2)
# Space Complexity: O(m)

from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}
        for num in nums2:
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)
        # Remaining elements have no next greater
        for num in stack:
            next_greater[num] = -1
        return [next_greater[num] for num in nums1]


# Alternate Python Solution: Brute Force
# - For each element in nums1, scan nums2 to find next greater element
# - Less efficient but simple

class SolutionBrute:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for x in nums1:
            index = nums2.index(x)
            next_val = -1
            for i in range(index + 1, len(nums2)):
                if nums2[i] > x:
                    next_val = nums2[i]
                    break
            res.append(next_val)
        return res


# Additional Examples (Edge Cases and Non-LeetCode Examples)

sol = Solution()

# Example 1: Normal case
print(sol.nextGreaterElement([4,1,2], [1,3,4,2]))
# Expected output: [-1,3,-1]

# Example 2: Single element
print(sol.nextGreaterElement([2], [1,2,3]))
# Expected output: [3]

# Example 3: All elements decreasing
print(sol.nextGreaterElement([3,2,1], [3,2,1]))
# Expected output: [-1,-1,-1]

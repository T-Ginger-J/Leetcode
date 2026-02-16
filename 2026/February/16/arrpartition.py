# LeetCode 561: Array Partition I
# Explanation:
# 1. Given an array of 2n integers, group these integers into n pairs (a, b) such that sum of min(a, b) for all pairs is maximized.
# 2. Approach:
#    - To maximize the sum of minimums, sort the array.
#    - Pair consecutive elements; sum every first element of each pair.
# 3. Time Complexity: O(n log n) for sorting
# 4. Space Complexity: O(1) or O(n) depending on sorting implementation

from typing import List

class Solution:

    # -------------------------------------------------------
    # Method 1: Sort and sum every other element
    # -------------------------------------------------------
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])

    # -------------------------------------------------------
    # Method 2: Counting sort optimization (for known value range)
    # -------------------------------------------------------
    def arrayPairSumCounting(self, nums: List[int]) -> int:
        offset = 10000  # nums[i] range: [-10000,10000]
        count = [0]*20001
        for num in nums:
            count[num + offset] += 1
        sum_min = 0
        take = True
        for i in range(20001):
            while count[i] > 0:
                if take:
                    sum_min += i - offset
                take = not take
                count[i] -= 1
        return sum_min


# -------------------------------------------------------
# Examples & Edge Cases
# -------------------------------------------------------

sol = Solution()

# Example 1
nums1 = [1,4,3,2]
print(sol.arrayPairSum(nums1))          # 4 (pairs: [1,2],[3,4], sum min = 1+3=4)
print(sol.arrayPairSumCounting(nums1))  # 4

# Example 2: negative numbers
nums2 = [-1,-2,-3,-4]
print(sol.arrayPairSum(nums2))          # -4 (pairs: [-4,-3],[-2,-1], sum min=-4+-2=-6? actually min sum=-4+-3=-7) let's compute
# Actually after sorting: [-4,-3,-2,-1], sum nums[::2] = -4 + -2 = -6
print(sol.arrayPairSum(nums2))          # -6

# Example 3: single pair
nums3 = [10,5]
print(sol.arrayPairSum(nums3))          # 5

# Example 4: already sorted
nums4 = [1,2,3,4,5,6]
print(sol.arrayPairSum(nums4))          # 9 (1+3+5)

# Example 5: repeated numbers
nums5 = [1,1,1,1]
print(sol.arrayPairSum(nums5))          # 2 (1+1)

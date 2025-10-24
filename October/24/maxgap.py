# LeetCode 164: Maximum Gap
# Explanation:
# 1. Given an unsorted array, find the maximum difference between successive elements in sorted form.
# 2. Sorting directly and finding max diff works in O(n log n).
# 3. Sort nums, then compute max(nums[i+1] - nums[i]).
# Time Complexity: O(n log n)
# Space Complexity: O(1) or O(n) depending on sorting algorithm

class Solution:
    def maximumGap(self, nums):
        if len(nums) < 2:
            return 0
        nums.sort()
        return max(nums[i+1] - nums[i] for i in range(len(nums) - 1))

    def maximumGapPigeonHole(self, nums):
        if len(nums) < 2:
            return 0
        min_val, max_val = min(nums), max(nums)
        if min_val == max_val:
            return 0
        
        n = len(nums)
        gap = math.ceil((max_val - min_val) / (n - 1))
        buckets = [[math.inf, -math.inf] for _ in range(n - 1)]
        
        for num in nums:
            if num == max_val:
                continue
            idx = (num - min_val) // gap
            buckets[idx][0] = min(buckets[idx][0], num)
            buckets[idx][1] = max(buckets[idx][1], num)
        
        max_gap = 0
        prev = min_val
        for b_min, b_max in buckets:
            if b_min == math.inf:
                continue
            max_gap = max(max_gap, b_min - prev)
            prev = b_max
        max_gap = max(max_gap, max_val - prev)
        return max_gap

print(Solution().maximumGap([3,6,9,1]))
# Output: 3  (sorted = [1,3,6,9], gaps = [2,3,3])

print(Solution().maximumGap([10]))
# Output: 0  (only one element)

print(Solution().maximumGap([1,10000000]))
# Output: 9999999

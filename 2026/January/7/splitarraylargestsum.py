# LeetCode 410: Split Array Largest Sum
# Explanation:
# 1. Binary search over possible max sums
# 2. Greedily check if mid allows <= m splits
# Time Complexity: O(n log(sum(nums)))
# Space Complexity: O(1)

class Solution:
    def splitArray(self, nums: list[int], m: int) -> int:
        def can_split(max_sum: int) -> bool:
            count, total = 1, 0
            for num in nums:
                total += num
                if total > max_sum:
                    total = num
                    count += 1
                    if count > m:
                        return False
            return True

        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if can_split(mid):
                right = mid
            else:
                left = mid + 1
        return left

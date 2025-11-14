# LeetCode 229: Majority Element II
# Explanation:
# 1. We count frequencies of all numbers using a dictionary.
# 2. Any number that appears more than floor(n/3) times is a majority element.
#
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
        from collections import Counter
        count = Counter(nums)
        threshold = len(nums) // 3
        return [x for x, c in count.items() if c > threshold]

    def majorityElementOneLine(self, nums: list[int]) -> list[int]:
        return [x for x in set(nums) if nums.count(x) > len(nums)//3]


# Example usage:
# sol = Solution()
# print(sol.majorityElement([3,2,3]))         # [3]
# print(sol.majorityElement([1,1,1,3,3,2,2])) # [1,2]

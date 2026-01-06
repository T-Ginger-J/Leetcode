# LeetCode 217: Contains Duplicate
# Explanation:
# 1. Use a set to track seen numbers.
# 2. If a number repeats, return True immediately.
# 3. Otherwise, return False at the end.
# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

    def containsDuplicateSet(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))
    
sol = Solution()
print(sol.containsDuplicate([1,2,3,1]))               # True
print(sol.containsDuplicate([1,2,3,4]))               # False
print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))   # True

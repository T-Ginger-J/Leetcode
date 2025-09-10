#O(n)
from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # Place each number x in position x-1
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        
        # Find the first position where nums[i] != i + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1
    

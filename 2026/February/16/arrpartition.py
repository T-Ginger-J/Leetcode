
class Solution:

    # -------------------------------------------------------
    # Method 1: Sort and sum every other element
    # -------------------------------------------------------
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return sum(nums[::2])


# LeetCode 228: Summary Ranges
# Explanation:
# 1. Iterate through the numbers and detect when ranges start and end.
# 2. When nums[i] != nums[i-1] + 1, we close a range.
# 3. Add either "x" or "x->y" depending on length of the range.
#
# Time Complexity: O(n)
# Space Complexity: O(1) besides output list.

class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        res = []
        if not nums:
            return res
        
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if start == nums[i - 1]:
                    res.append(str(start))
                else:
                    res.append(f"{start}->{nums[i - 1]}")
                start = nums[i]

        # close last range
        if start == nums[-1]:
            res.append(str(start))
        else:
            res.append(f"{start}->{nums[-1]}")

        return res


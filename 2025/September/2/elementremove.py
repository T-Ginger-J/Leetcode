class Solution:
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
    
    def removeElementOneLine(self, nums, val):
        nums[:] = [x for x in nums if x != val]; return len(nums)


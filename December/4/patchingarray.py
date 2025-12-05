class Solution:
    def minPatches(self, nums, n):
        miss = 1     # smallest number that cannot yet be formed
        patches = 0
        i = 0

        while miss <= n:
            if i < len(nums) and nums[i] <= miss:
                miss += nums[i]
                i += 1
            else:
                # patch with 'miss'
                miss += miss
                patches += 1

        return patches

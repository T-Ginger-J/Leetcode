class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = float('inf')
        
        for i in range(n):
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if abs(total - target) < abs(closest - target):
                    closest = total
                
                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total  # exact match
        return closest

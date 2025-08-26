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

    def threeSumClosestPruning(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]
        
        for i in range(n-2):
            # Skip duplicates (optional but saves time)
            if i > 0 and nums[i] == nums[i-1]:
                continue

            # Prune: smallest possible sum > target
            if nums[i] + nums[i+1] + nums[i+2] > target:
                if abs(nums[i] + nums[i+1] + nums[i+2] - target) < abs(closest - target):
                    closest = nums[i] + nums[i+1] + nums[i+2]
                break
            
            # Prune: largest possible sum < target
            if nums[i] + nums[n-2] + nums[n-1] < target:
                if abs(nums[i] + nums[n-2] + nums[n-1] - target) < abs(closest - target):
                    closest = nums[i] + nums[n-2] + nums[n-1]
                continue

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

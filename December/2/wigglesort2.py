# LeetCode 324: Wiggle Sort II
# Explanation:
# We want: nums[0] < nums[1] > nums[2] < nums[3] ...
#
# Method (O(n)):
# 1. Find the median using nth_element / quickselect.
# 2. 3-way partition (Dutch National Flag) around the median BUT using
#    "virtual indexing" which maps indices as:
#
#       mapped(i) = (1 + 2*i) % (n | 1)
#
#    to place larger values in odd positions and smaller values in even positions
#    without violating movement during partition.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def wiggleSort(self, nums):
        import random
        
        def nth_element(nums, n):
            # Quickselect to find nth smallest value
            def select(left, right, k):
                if left == right:
                    return nums[left]
                pivot = nums[random.randint(left, right)]
                l, r = left, right
                i = left
                while i <= r:
                    if nums[i] < pivot:
                        nums[l], nums[i] = nums[i], nums[l]
                        l += 1; i += 1
                    elif nums[i] > pivot:
                        nums[r], nums[i] = nums[i], nums[r]
                        r -= 1
                    else:
                        i += 1
                if k < l:
                    return select(left, l - 1, k)
                elif k > r:
                    return select(r + 1, right, k)
                else:
                    return nums[k]
            return select(0, len(nums) - 1, n)
        
        n = len(nums)
        if n <= 1:
            return
        
        median = nth_element(nums[:], n // 2)
        
        def idx(i): return (1 + 2*i) % (n | 1)
        
        i = j = 0
        k = n - 1
        
        while j <= k:
            if nums[idx(j)] > median:
                nums[idx(i)], nums[idx(j)] = nums[idx(j)], nums[idx(i)]
                i += 1; j += 1
            elif nums[idx(j)] < median:
                nums[idx(j)], nums[idx(k)] = nums[idx(k)], nums[idx(j)]
                k -= 1
            else:
                j += 1


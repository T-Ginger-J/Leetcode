# LeetCode 327: Count of Range Sum
# Explanation:
# 1. Build prefix sums: ps[i] = sum(nums[0:i])
# 2. We need to count pairs (i < j) such that:
#       lower ≤ ps[j] - ps[i] ≤ upper
# 3. Use a modified merge sort:
#    - During merge, count how many left-side prefix sums fall in the valid range
#      for each right-side prefix sum.
# 4. Sort helps maintain prefix sums in order for efficient counting.
#
# Time Complexity: O(n log n)
# Space Complexity: O(n)

class Solution:
    def countRangeSum(self, nums, lower, upper):
        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + x)

        def merge_sort(lo, hi):
            if hi - lo <= 1:
                return 0
            mid = (lo + hi) // 2
            cnt = merge_sort(lo, mid) + merge_sort(mid, hi)
            
            j = k = mid
            temp = []
            i = lo
            
            # Count valid ranges
            for left_val in prefix[lo:mid]:
                while k < hi and prefix[k] - left_val < lower:
                    k += 1
                while j < hi and prefix[j] - left_val <= upper:
                    j += 1
                cnt += j - k

            # Merge step
            l, r = lo, mid
            while l < mid and r < hi:
                if prefix[l] < prefix[r]:
                    temp.append(prefix[l])
                    l += 1
                else:
                    temp.append(prefix[r])
                    r += 1
            temp.extend(prefix[l:mid])
            temp.extend(prefix[r:hi])
            prefix[lo:hi] = temp

            return cnt

        return merge_sort(0, len(prefix))

# LeetCode 300: Longest Increasing Subsequence
# Explanation:
# 1. Use dynamic programming to find LIS ending at each index.
# 2. dp[i] = length of longest increasing subsequence ending at nums[i].
# 3. For each i, check all j < i:
#    - If nums[i] > nums[j], dp[i] = max(dp[i], dp[j]+1)
# 4. Answer = max(dp)
# Time Complexity: O(n^2)
# Space Complexity: O(n)

import bisect, functools

class Solution:
    def lengthOfLIS(self, nums):
        if not nums: return 0
        n = len(nums)
        dp = [1]*n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

    def lengthOfLISBinSearch(self, nums):
        sub = []
        for x in nums:
            i = bisect.bisect_left(sub, x)
            if i == len(sub):
                sub.append(x)
            else:
                sub[i] = x
        return len(sub)
    
    lengthOfLISOneLine = lambda self, nums: functools.reduce(lambda sub,x: sub+[x] if not sub or x>sub[-1] else sub[:bisect.bisect_left(sub,x)]+[x]+sub[bisect.bisect_left(sub,x)+1:], nums, []) and len(functools.reduce(lambda sub,x: sub+[x] if not sub or x>sub[-1] else sub[:bisect.bisect_left(sub,x)]+[x]+sub[bisect.bisect_left(sub,x)+1:], nums, []))

print(Solution().lengthOfLIS([10,9,2,5,3,7,101,18])) # 4 ([2,3,7,101])
print(Solution().lengthOfLIS([0,1,0,3,2,3]))         # 4 ([0,1,2,3])
print(Solution().lengthOfLIS([7,7,7,7,7,7,7]))       # 1

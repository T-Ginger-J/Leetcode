# LeetCode 523: Continuous Subarray Sum
# Explanation:
# 1. We are given an integer array nums and an integer k.
# 2. We must check if there exists a subarray of length at least 2
#    whose sum is a multiple of k.
# 3. Use prefix sums and modular arithmetic.

# Methods Used:
# - Prefix Sum + Hash Map (Remainder Tracking)
# - Brute Force (For Comparison)

# Key Idea:
# - If two prefix sums have the same remainder mod k,
#   their difference is divisible by k.

# Time Complexity:
# - Hash Map Method: O(n)
# - Brute Force: O(n^2)

# Space Complexity:
# - O(min(n, k))


from typing import List


class Solution:

    # -------------------------------------------------------
    # Method 1: Prefix Sum + Hash Map (Optimal)
    # -------------------------------------------------------
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        rem_index = {0: -1}   # remainder -> earliest index
        prefix = 0

        for i, num in enumerate(nums):

            prefix += num

            if k != 0:
                prefix %= k

            if prefix in rem_index:

                # Subarray length >= 2
                if i - rem_index[prefix] >= 2:
                    return True

            else:
                rem_index[prefix] = i

        return False

    # -------------------------------------------------------
    # Method 2: Brute Force (For Understanding)
    # -------------------------------------------------------
    def checkSubarraySumBrute(self, nums: List[int], k: int) -> bool:

        n = len(nums)

        for i in range(n):
            total = nums[i]

            for j in range(i + 1, n):

                total += nums[j]

                if k == 0:
                    if total == 0:
                        return True
                else:
                    if total % k == 0:
                        return True

        return False


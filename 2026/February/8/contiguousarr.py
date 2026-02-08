# LeetCode 525: Contiguous Array
# Explanation:
# 1. Given a binary array, find the length of the longest contiguous subarray
#    with equal number of 0s and 1s.
# 2. Transform 0s to -1s. Then the problem reduces to finding the longest subarray
#    with sum 0.
# 3. Use prefix sum + hashmap to store earliest occurrence of each sum.

# Methods Used:
# - Prefix Sum + Hash Map (Optimal)
# - Brute Force (O(n^2), for understanding)

# Time Complexity:
# - Hash Map: O(n)
# - Brute Force: O(n^2)

# Space Complexity:
# - O(n) for Hash Map


from typing import List


class Solution:

    # -------------------------------------------------------
    # Method 1: Prefix Sum + Hash Map (Optimal)
    # -------------------------------------------------------
    def findMaxLength(self, nums: List[int]) -> int:

        prefix_sum = 0
        max_len = 0
        sum_index = {0: -1}  # sum -> earliest index

        for i, num in enumerate(nums):

            # Treat 0 as -1
            prefix_sum += 1 if num == 1 else -1

            if prefix_sum in sum_index:
                max_len = max(max_len, i - sum_index[prefix_sum])
            else:
                sum_index[prefix_sum] = i

        return max_len

    # -------------------------------------------------------
    # Method 2: Brute Force (For Understanding)
    # -------------------------------------------------------
    def findMaxLengthBrute(self, nums: List[int]) -> int:

        n = len(nums)
        max_len = 0

        for i in range(n):
            count0 = 0
            count1 = 0

            for j in range(i, n):
                if nums[j] == 0:
                    count0 += 1
                else:
                    count1 += 1

                if count0 == count1:
                    max_len = max(max_len, j - i + 1)

        return max_len


# -------------------------------------------------------
# Examples (Including Edge Cases)
# -------------------------------------------------------

# Example 1
print(Solution().findMaxLength([0, 1]))                   # 2

# Example 2
print(Solution().findMaxLength([0, 1, 0]))                # 2

# Example 3 (All zeros)
print(Solution().findMaxLength([0, 0, 0, 0]))             # 0

# Example 4 (All ones)
print(Solution().findMaxLength([1, 1, 1, 1]))             # 0

# Example 5 (Long Mixed)
print(Solution().findMaxLength([0, 1, 1, 0, 1, 0, 0]))    # 6

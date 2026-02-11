# LeetCode 541: Reverse String II
# Explanation:
# 1. Given a string s and integer k, reverse the first k characters for every 2k characters.
# 2. If less than k characters remain, reverse all of them.
# 3. If between k and 2k characters remain, reverse the first k and leave the rest.

# Methods Used:
# - Iterate in steps of 2k
# - Reverse slices of the string
# - Join back to result

# Time Complexity:
# - O(n), n = length of string

# Space Complexity:
# - O(n) for result string


class Solution:

    # -------------------------------------------------------
    # Method 1: Slice Reversal
    # -------------------------------------------------------
    def reverseStr(self, s: str, k: int) -> str:

        s = list(s)
        n = len(s)

        for i in range(0, n, 2 * k):
            s[i:i+k] = reversed(s[i:i+k])

        return ''.join(s)


# LeetCode 556: Next Greater Element III
# Explanation:
# 1. Given a positive integer n, find the smallest integer greater than n using the same digits.
# 2. Approach (Next Permutation):
#    - Convert number to a list of digits.
#    - Traverse from right to left to find the first digit 'i' where digits[i] < digits[i+1].
#    - Find the smallest digit after i that is larger than digits[i] and swap.
#    - Reverse the sublist after i to get the smallest next number.
#    - If no such i exists, return -1 (digits are in descending order).
# 3. Time Complexity: O(k), k = number of digits
# 4. Space Complexity: O(k)

class Solution:

    # -------------------------------------------------------
    # Method 1: Next Permutation
    # -------------------------------------------------------
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        i = len(digits) - 2
        while i >= 0 and digits[i] >= digits[i+1]:
            i -= 1
        if i < 0:
            return -1
        # find smallest digit > digits[i] on the right
        j = len(digits) - 1
        while digits[j] <= digits[i]:
            j -= 1
        digits[i], digits[j] = digits[j], digits[i]
        digits[i+1:] = reversed(digits[i+1:])
        res = int(''.join(digits))
        return res if res <= 2**31 - 1 else -1


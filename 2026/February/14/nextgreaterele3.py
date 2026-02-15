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


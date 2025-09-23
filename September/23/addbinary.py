# LeetCode 67: Add Binary
# Explanation:
# 1. Simulate binary addition from right to left with carry.
# 2. Append digits to result and reverse at the end.
# Time Complexity: O(max(len(a), len(b)))
# Space Complexity: O(max(len(a), len(b)))

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j, carry = len(a)-1, len(b)-1, 0
        res = []
        while i >= 0 or j >= 0 or carry:
            total = carry
            if i >= 0:
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            res.append(str(total % 2))
            carry = total // 2
        return "".join(reversed(res))
    
    def addBinaryBuiltIn(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

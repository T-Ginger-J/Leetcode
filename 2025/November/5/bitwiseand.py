# LeetCode 201: Bitwise AND of Numbers Range
# Explanation:
# 1. Keep right-shifting both left and right until they are equal.
# 2. Count how many shifts are done.
# 3. Shift back to left to get the common prefix.
# Time Complexity: O(log n)
# Space Complexity: O(1)

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left < right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift
    
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right > left:
            right &= (right - 1)
        return right

    def rangeBitwiseAndOneLine(self, l, r): return r & (0 if l<r else l)

sol = Solution()
print(sol.rangeBitwiseAnd(5, 7))        # 4
print(sol.rangeBitwiseAnd(0, 0))        # 0
print(sol.rangeBitwiseAnd(1, 2147483647))  # 0

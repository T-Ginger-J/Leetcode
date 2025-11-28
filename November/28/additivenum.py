# LeetCode 306: Additive Number
# Explanation:
# 1. An additive number sequence has at least 3 numbers where each number is the sum of the previous two.
# 2. Use backtracking to try all splits for first two numbers.
# 3. Avoid numbers with leading zeros unless the number is 0.
# 4. Check if the remaining string can form a valid additive sequence recursively.
# Time Complexity: O(n^2 * 2^n), trying all splits and recursive checks
# Space Complexity: O(n) recursion stack

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        
        def is_valid(x):
            return not (x.startswith('0') and len(x) > 1)
        
        def dfs(num1, num2, remaining):
            if not remaining:
                return True
            sum_str = str(int(num1) + int(num2))
            if remaining.startswith(sum_str):
                return dfs(num2, sum_str, remaining[len(sum_str):])
            return False
        
        for i in range(1, n):
            for j in range(i+1, n):
                num1, num2, remaining = num[:i], num[i:j], num[j:]
                if is_valid(num1) and is_valid(num2):
                    if dfs(num1, num2, remaining):
                        return True
        return False

print(Solution().isAdditiveNumber("112358"))  # True (1,1,2,3,5,8)
print(Solution().isAdditiveNumber("199100199")) # True (1,99,100,199)
print(Solution().isAdditiveNumber("123"))       # True (1,2,3)
print(Solution().isAdditiveNumber("1023"))      # False

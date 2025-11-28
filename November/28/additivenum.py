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

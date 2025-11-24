# LeetCode 282: Expression Add Operators
# Explanation:
# 1. We are asked to insert '+', '-', '*' operators between digits to reach a target value.
# 2. Use backtracking / DFS to explore all possibilities:
#    - Keep track of the current expression string, current value, and previous number (for multiplication).
#    - At each step, decide to add '+', '-', or '*' before the next number.
#    - Skip numbers with leading zeroes.
# 3. Append expression to result if end of string is reached and value matches target.
# Time Complexity: O(4^(n-1)) in worst case (every gap can have 4 choices: '+', '-', '*', nothing)
# Space Complexity: O(n) recursion stack + O(4^(n-1)) for storing expressions

class Solution:
    def addOperators(self, num: str, target: int):
        res = []

        def dfs(index, path, value, prev):
            if index == len(num):
                if value == target:
                    res.append(path)
                return
            for i in range(index+1, len(num)+1):
                tmp = num[index:i]
                if len(tmp) > 1 and tmp[0] == '0':
                    break
                n = int(tmp)
                if index == 0:
                    dfs(i, tmp, n, n)
                else:
                    dfs(i, path+'+'+tmp, value+n, n)
                    dfs(i, path+'-'+tmp, value-n, -n)
                    dfs(i, path+'*'+tmp, value-prev+prev*n, prev*n)

        dfs(0, '', 0, 0)
        return res

    def addOperatorsPruning(self, num: str, target: int):
        res = []
        n = len(num)

        def dfs(i, expr, val, last):
            if i == n:
                if val == target:
                    res.append(expr)
                return
            for j in range(i, n):
                if j > i and num[i] == '0':
                    break
                curr = int(num[i:j+1])
                if i == 0:
                    dfs(j+1, str(curr), curr, curr)
                else:
                    dfs(j+1, expr+'+'+str(curr), val+curr, curr)
                    dfs(j+1, expr+'-'+str(curr), val-curr, -curr)
                    dfs(j+1, expr+'*'+str(curr), val-last+last*curr, last*curr)

        dfs(0, '', 0, 0)
        return res

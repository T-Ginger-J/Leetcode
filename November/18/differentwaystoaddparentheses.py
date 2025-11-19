
class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:
        memo = {}

        def compute(expr):
            if expr in memo:
                return memo[expr]
            
            results = []
            for i, ch in enumerate(expr):
                if ch in "+-*":
                    left = compute(expr[:i])
                    right = compute(expr[i+1:])
                    for a in left:
                        for b in right:
                            if ch == '+':
                                results.append(a + b)
                            elif ch == '-':
                                results.append(a - b)
                            else:  # '*'
                                results.append(a * b)

            if not results:          # expr is a number
                results = [int(expr)]

            memo[expr] = results
            return results
        
        return compute(expression)


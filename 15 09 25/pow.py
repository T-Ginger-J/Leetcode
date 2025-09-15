class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n < 0: 
            x, n = 1 / x, -n
        res = 1
        while n:
            if n & 1:
                res *= x
            x *= x
            n >>= 1
        return res

    def myPowRecursive(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n < 0: return 1 / self.myPow(x, -n)
        half = self.myPow(x, n // 2)
        return half * half if n % 2 == 0 else half * half * x
    
    def myPowOneLine(self, x: float, n: int) -> float:
        return 1 if n==0 else self.myPow(x*x, n//2)*(x if n%2 else 1) if n>0 else 1/self.myPow(x,-n)



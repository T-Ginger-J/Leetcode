class Solution:
    def totalNQueens(self, n: int) -> int:
        cols, diag1, diag2 = set(), set(), set()
        count = 0

        def backtrack(r: int):
            nonlocal count
            if r == n:
                count += 1
                return
            for c in range(n):
                if c in cols or r-c in diag1 or r+c in diag2: 
                    continue
                cols.add(c); diag1.add(r-c); diag2.add(r+c)
                backtrack(r+1)
                cols.remove(c); diag1.remove(r-c); diag2.remove(r+c)

        backtrack(0)
        return count

    def totalNQueensBitmask(self, n: int) -> int:
        self.count = 0

        def backtrack(r: int, cols: int, d1: int, d2: int):
            if r == n:
                self.count += 1
                return
            available = ((1 << n) - 1) & ~(cols | d1 | d2)
            while available:
                bit = available & -available  # pick rightmost 1
                available -= bit
                backtrack(r + 1, cols | bit, (d1 | bit) << 1, (d2 | bit) >> 1)

        backtrack(0, 0, 0, 0)
        return self.count
    
totalNQueens=lambda n:(f:=lambda r,c,d1,d2: r==n or sum(f(r+1,c|b,(d1|b)<<1,(d2|b)>>1) for b in [x&-x for x in [((1<<n)-1)&~(c|d1|d2)]] for _ in iter(int,1) if not (x:=x-b))) (0,0,0,0)



print(Solution().totalNQueens(4))  # Output: 2
print(Solution().totalNQueens(1))  # Output: 1
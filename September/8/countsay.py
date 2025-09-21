#O(n^2)
class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n - 1):
            next_s = []
            i = 0
            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i] == s[i + 1]:
                    count += 1
                    i += 1
                next_s.append(str(count))
                next_s.append(s[i])
                i += 1
            s = "".join(next_s)
        return s

    def countAndSayOneLine(self, n: int) -> str:
        return "1" if n == 1 else "".join(str(len(list(g))) + d for d, g in __import__("itertools").groupby(self.countAndSay(n - 1)))

    def countAndSayOptimized(self, n: int) -> str:
        s = "1"
        for _ in range(n - 1):
            res = []
            prev = s[0]
            count = 1
            for c in s[1:]:
                if c == prev:
                    count += 1
                else:
                    res.append(str(count))
                    res.append(prev)
                    prev = c
                    count = 1
            res.append(str(count))
            res.append(prev)
            s = "".join(res)
        return s

class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 0:
            return 0
        if n <= 3:
            return 1

        s = [1, 2, 2]
        i = 2
        num = 1

        while len(s) < n:
            count = s[i]
            s.extend([num] * count)
            num = 3 - num
            i += 1

        return s[:n].count(1)



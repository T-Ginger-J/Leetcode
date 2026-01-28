class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)
        max_m = n.bit_length() - 1  # maximum length of representation

        for m in range(max_m, 1, -1):
            left, right = 2, int(n ** (1/m)) + 1
            while left <= right:
                k = (left + right) // 2
                s = (k ** (m + 1) - 1) // (k - 1)
                if s == n:
                    return str(k)
                elif s < n:
                    left = k + 1
                else:
                    right = k - 1

        return str(n - 1)  # default base for 1+1+...+1 representation


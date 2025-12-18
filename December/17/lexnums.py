class Solution:
    def lexicalOrder(self, n: int) -> list[int]:
        res = []

        def dfs(curr):
            if curr > n:
                return
            res.append(curr)
            for i in range(10):
                next_num = curr * 10 + i
                if next_num > n:
                    return
                dfs(next_num)

        for i in range(1, 10):
            dfs(i)
        return res
